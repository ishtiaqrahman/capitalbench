from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from capitalbench.cli import main
from capitalbench.io import load_options_file
from capitalbench.prompting import build_prompt
from capitalbench.schemas import MarketOption
from capitalbench.universe import validate_universe


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UNIVERSE_PATH = PROJECT_ROOT / "configs" / "universes" / "capitalbench_universe_v1_5.yaml"
UNIVERSE_V2_PATH = PROJECT_ROOT / "configs" / "universes" / "capitalbench_universe_v2_0.yaml"
UNIVERSE_V2_ADDED_SYMBOLS = [
    "RSP",
    "XBI",
    "KRE",
    "ITA",
    "EWC",
    "EWU",
    "EWA",
    "EWY",
    "EWT",
    "EWZ",
    "EWW",
    "EZA",
    "MBB",
    "MUB",
    "EMB",
    "BNDX",
    "SLV",
    "CPER",
    "DBA",
    "USO",
    "UUP",
    "FXE",
    "FXY",
    "IBIT",
    "ETHA",
]


def _write_small_universe(path: Path) -> Path:
    path.write_text(
        yaml.safe_dump(
            {
                "options": [
                    {
                        "id": "CASH",
                        "name": "Cash",
                        "symbol": None,
                        "tiingo_symbol": None,
                        "asset_class": "cash",
                        "category": "cash",
                        "option_group": "cash",
                        "risk_bucket": "cash",
                        "currency": "USD",
                        "is_cash": True,
                        "include_in_universe": True,
                        "exposure_description": "Cash position with no market exposure.",
                    },
                    {
                        "id": "SP500",
                        "name": "S&P 500",
                        "symbol": "SPY",
                        "tiingo_symbol": "SPY",
                        "asset_class": "equity",
                        "category": "broad_us_equity",
                        "option_group": "us_broad_market",
                        "risk_bucket": "medium",
                        "currency": "USD",
                        "is_cash": False,
                        "include_in_universe": True,
                        "exposure_description": "Broad US large-cap equity exposure.",
                    },
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


def test_v1_5_options_schema_accepts_full_universe() -> None:
    options = load_options_file(UNIVERSE_PATH)

    assert len(options) == 40
    assert options[0].id == "CASH"
    assert options[-1].id == "SOFTWARE"


def test_v2_0_options_schema_accepts_expanded_universe() -> None:
    v1_options = load_options_file(UNIVERSE_PATH)
    v2_options = load_options_file(UNIVERSE_V2_PATH)

    assert len(v2_options) == 65
    assert [option.id for option in v2_options[:40]] == [option.id for option in v1_options]
    assert [option.symbol for option in v2_options[-25:]] == UNIVERSE_V2_ADDED_SYMBOLS
    assert len({option.id for option in v2_options}) == 65
    assert len({option.symbol for option in v2_options if not option.is_cash}) == 64
    assert sum(option.is_cash for option in v2_options) == 1
    assert sum(option.is_benchmark for option in v2_options) == 1
    assert all(option.tiingo_symbol for option in v2_options if not option.is_cash)


def test_cash_can_have_null_symbol_and_tiingo_symbol() -> None:
    option = MarketOption.model_validate(
        {
            "id": "CASH",
            "name": "Cash",
            "symbol": None,
            "tiingo_symbol": None,
            "asset_class": "cash",
            "category": "cash",
            "option_group": "cash",
            "risk_bucket": "cash",
            "currency": "USD",
            "is_cash": True,
            "include_in_universe": True,
            "exposure_description": "Cash position with no market exposure.",
        }
    )

    assert option.symbol is None
    assert option.tiingo_symbol is None


def test_non_cash_option_requires_symbol_and_tiingo_symbol() -> None:
    with pytest.raises(ValidationError):
        MarketOption.model_validate(
            {
                "id": "SP500",
                "name": "S&P 500",
                "symbol": "SPY",
                "tiingo_symbol": None,
                "asset_class": "equity",
                "category": "broad_us_equity",
                "option_group": "us_broad_market",
                "risk_bucket": "medium",
                "currency": "USD",
                "is_cash": False,
                "include_in_universe": True,
                "exposure_description": "Broad US large-cap equity exposure.",
            }
        )


def test_prompt_rendering_includes_descriptions_and_hides_internal_fields(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    round_path.mkdir()
    (round_path / "prompt.md").write_text("Choose one option.", encoding="utf-8")
    (round_path / "briefing.md").write_text("Briefing.", encoding="utf-8")
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test-round",
                "title": "Test Round",
                "decision_date": "2026-01-01",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Use entry prices.",
                "exit_rule": "Use exit prices.",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_small_universe(round_path / "options.yaml")

    prompt = build_prompt(round_path)

    assert "## Round Metadata" in prompt
    assert "Round ID: test-round" in prompt
    assert "Scoring window: 2026-01-02 to 2026-02-02; optimize for this one month window only." in prompt
    assert "Scoring benchmark: S&P 500 / SPY" in prompt
    assert "Symbol: N/A" in prompt
    assert "Description: Broad US large-cap equity exposure." in prompt
    assert "Risk bucket: medium" in prompt
    assert "include_in_universe" not in prompt
    assert "tiingo_symbol" not in prompt


def test_prompt_rendering_includes_frozen_universe_performance_when_present(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    round_path.mkdir()
    (round_path / "prompt.md").write_text("Choose one option.", encoding="utf-8")
    (round_path / "briefing.md").write_text("Briefing.", encoding="utf-8")
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test-round",
                "title": "Test Round",
                "decision_date": "2026-01-01",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Use entry prices.",
                "exit_rule": "Use exit prices.",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_small_universe(round_path / "options.yaml")
    market_data_dir = round_path / "market_data"
    market_data_dir.mkdir()
    (market_data_dir / "universe_trailing_returns.md").write_text(
        "# Full-Universe Trailing Returns\n\n| option_id | return_7d |\n| --- | --- |\n| SP500 | 1.00% |\n",
        encoding="utf-8",
    )

    prompt = build_prompt(round_path)

    assert "## Full-Universe Trailing Returns" in prompt
    assert "| SP500 | 1.00% |" in prompt


def test_prompt_rendering_does_not_duplicate_embedded_universe_performance(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    round_path.mkdir()
    (round_path / "prompt.md").write_text("Choose one option.", encoding="utf-8")
    (round_path / "briefing.md").write_text(
        "Briefing.\n\n# Full-Universe Trailing Returns\n\n| option_id | return_7d |\n| --- | --- |\n| SP500 | 1.00% |\n",
        encoding="utf-8",
    )
    (round_path / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "round_id": "test-round",
                "title": "Test Round",
                "decision_date": "2026-01-01",
                "decision_deadline": "2026-01-01T20:00:00Z",
                "horizon": "one month",
                "entry_rule": "Use entry prices.",
                "exit_rule": "Use exit prices.",
                "entry_date": "2026-01-02",
                "exit_date": "2026-02-02",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    _write_small_universe(round_path / "options.yaml")
    market_data_dir = round_path / "market_data"
    market_data_dir.mkdir()
    (market_data_dir / "universe_trailing_returns.md").write_text(
        "# Full-Universe Trailing Returns\n\n| option_id | return_7d |\n| --- | --- |\n| SP500 | 2.00% |\n",
        encoding="utf-8",
    )

    prompt = build_prompt(round_path)

    assert prompt.count("# Full-Universe Trailing Returns") == 1
    assert "| SP500 | 1.00% |" in prompt
    assert "| SP500 | 2.00% |" not in prompt


def test_validate_universe_fails_clearly_when_tiingo_key_missing(tmp_path: Path, monkeypatch) -> None:
    options_path = _write_small_universe(tmp_path / "options.yaml")
    monkeypatch.delenv("TIINGO_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="TIINGO_API_KEY"):
        validate_universe(options_path=options_path, start_date="2026-01-01", end_date="2026-01-31")


def test_validate_universe_cli_fails_clearly_when_tiingo_key_missing(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    options_path = _write_small_universe(tmp_path / "options.yaml")
    monkeypatch.delenv("TIINGO_API_KEY", raising=False)

    exit_code = main(
        [
            "validate-universe",
            "--options",
            str(options_path),
            "--start-date",
            "2026-01-01",
            "--end-date",
            "2026-01-31",
        ]
    )
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "TIINGO_API_KEY" in captured.err


def test_validate_universe_skips_cash_and_passes_mocked_tiingo_response(tmp_path: Path, monkeypatch) -> None:
    options_path = _write_small_universe(tmp_path / "options.yaml")
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    output = validate_universe(
        options_path=options_path,
        start_date="2026-01-01",
        end_date="2026-01-31",
        fetcher=lambda symbol, start, end, key: [
            {"date": "2026-01-02T00:00:00.000Z", "close": 100.0, "adjClose": 100.0}
        ],
    )

    statuses = {result["id"]: result["status"] for result in output.report["results"]}
    assert statuses == {"CASH": "skipped_cash", "SP500": "pass"}
    assert output.json_path.exists()
    assert output.markdown_path.exists()
    assert output.json_path.name == "options_validation_report.json"


def test_validate_universe_fails_mocked_tiingo_response_with_no_rows(tmp_path: Path, monkeypatch) -> None:
    options_path = _write_small_universe(tmp_path / "options.yaml")
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    output = validate_universe(
        options_path=options_path,
        start_date="2026-01-01",
        end_date="2026-01-31",
        fetcher=lambda symbol, start, end, key: [],
    )

    sp500 = next(result for result in output.report["results"] if result["id"] == "SP500")
    assert sp500["status"] == "fail"
    assert "no price rows" in sp500["message"]


def test_validate_universe_fails_mocked_tiingo_response_with_missing_adj_close(
    tmp_path: Path,
    monkeypatch,
) -> None:
    options_path = _write_small_universe(tmp_path / "options.yaml")
    monkeypatch.setenv("TIINGO_API_KEY", "test-key")

    output = validate_universe(
        options_path=options_path,
        start_date="2026-01-01",
        end_date="2026-01-31",
        fetcher=lambda symbol, start, end, key: [
            {"date": "2026-01-02T00:00:00.000Z", "close": 100.0}
        ],
    )

    sp500 = next(result for result in output.report["results"] if result["id"] == "SP500")
    assert sp500["status"] == "fail"
    assert "adjClose" in sp500["message"]


def test_init_round_universe_copies_options_yaml(tmp_path: Path) -> None:
    exit_code = main(
        [
            "init-round",
            "--round-id",
            "CB-TEST-UNIVERSE",
            "--rounds-dir",
            str(tmp_path / "rounds"),
            "--universe",
            str(UNIVERSE_PATH),
        ]
    )

    copied = tmp_path / "rounds" / "CB-TEST-UNIVERSE" / "options.yaml"
    manifest = yaml.safe_load((tmp_path / "rounds" / "CB-TEST-UNIVERSE" / "manifest.yaml").read_text(encoding="utf-8"))
    assert exit_code == 0
    assert copied.read_text(encoding="utf-8") == UNIVERSE_PATH.read_text(encoding="utf-8")
    assert manifest["universe_version"] == "capitalbench_universe_v1_5"


def test_init_round_allows_explicit_universe_version(tmp_path: Path) -> None:
    exit_code = main(
        [
            "init-round",
            "--round-id",
            "CB-TEST-UNIVERSE-VERSION",
            "--rounds-dir",
            str(tmp_path / "rounds"),
            "--universe",
            str(UNIVERSE_V2_PATH),
            "--universe-version",
            "v2.0",
        ]
    )

    manifest = yaml.safe_load(
        (tmp_path / "rounds" / "CB-TEST-UNIVERSE-VERSION" / "manifest.yaml").read_text(encoding="utf-8")
    )
    assert exit_code == 0
    assert manifest["universe_version"] == "v2.0"


def test_init_round_prompt_allows_internal_knowledge_but_blocks_live_retrieval(tmp_path: Path) -> None:
    exit_code = main(
        [
            "init-round",
            "--round-id",
            "CB-TEST-PROMPT",
            "--rounds-dir",
            str(tmp_path / "rounds"),
        ]
    )

    prompt = (tmp_path / "rounds" / "CB-TEST-PROMPT" / "prompt.md").read_text(encoding="utf-8")
    assert exit_code == 0
    assert "internal learned knowledge and general market priors" in prompt
    assert "Do not browse, use tools, request updated market data" in prompt
    assert "close-to-close one-month scoring window" in prompt
    assert "calculated after regular trading ends on the exit date" in prompt
    assert "Use longer-horizon facts only when they are likely to affect prices before the exit close." in prompt
    assert "strongest expected one-month realized return" in prompt
    assert "Use only the information in this prompt" not in prompt


def test_init_round_can_create_portfolio_protocol_round(tmp_path: Path) -> None:
    exit_code = main(
        [
            "init-round",
            "--round-id",
            "CB-TEST-PORTFOLIO",
            "--rounds-dir",
            str(tmp_path / "rounds"),
            "--submission-format",
            "portfolio",
        ]
    )

    round_path = tmp_path / "rounds" / "CB-TEST-PORTFOLIO"
    manifest = yaml.safe_load((round_path / "manifest.yaml").read_text(encoding="utf-8"))
    prompt = (round_path / "prompt.md").read_text(encoding="utf-8")
    assert exit_code == 0
    assert manifest["submission_format"] == "portfolio"
    assert manifest["methodology_version"] == "portfolio-v1.0"
    assert "portfolio" in prompt
    assert "maximize expected one-month realized portfolio return" in prompt
    assert "close-to-close one-month scoring window" in prompt
    assert "calculated after regular trading ends on the exit date" in prompt
    assert "Use longer-horizon facts only when they are likely to affect prices before the exit close." in prompt
    assert "allocation_pct values must sum to exactly 100" in prompt
