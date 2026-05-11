import hashlib
from pathlib import Path

from capitalbench.hashing import compute_round_hashes, write_round_hashes
from capitalbench.io import read_json


def test_hashing_determinism(tmp_path: Path) -> None:
    round_path = tmp_path / "round"
    round_path.mkdir()
    files = {
        "briefing.md": "briefing\n",
        "options.yaml": "options: []\n",
        "prompt.md": "prompt\n",
        "manifest.yaml": "round_id: test\n",
    }
    for filename, content in files.items():
        (round_path / filename).write_text(content, encoding="utf-8")
    market_data_dir = round_path / "market_data"
    market_data_dir.mkdir()
    (market_data_dir / "universe_trailing_returns.md").write_text("returns\n", encoding="utf-8")

    first = compute_round_hashes(round_path)
    second = compute_round_hashes(round_path)
    written = write_round_hashes(round_path)

    assert first == second == written
    assert read_json(round_path / "hashes.json") == first
    expected_briefing_hash = hashlib.sha256(files["briefing.md"].encode("utf-8")).hexdigest()
    assert first["files"]["briefing.md"] == expected_briefing_hash
    assert "market_data/universe_trailing_returns.md" in first["files"]
