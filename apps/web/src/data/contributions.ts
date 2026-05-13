export type ContributionTier = {
  name: string;
  amount: string;
  cadence: "monthly" | "one-time";
  description: string;
  href: string;
  cta: string;
  featured?: boolean;
};

export const monthlyContributionTiers: ContributionTier[] = [
  {
    name: "Individual",
    amount: "$10",
    cadence: "monthly",
    description: "A lightweight recurring contribution for readers who want CapitalBench to keep publishing public rounds.",
    href: "https://buy.stripe.com/7sY28s74kbXLaUm9tP24000",
    cta: "Contribute $10/mo"
  },
  {
    name: "Backer",
    amount: "$25",
    cadence: "monthly",
    description: "Steady funding for model API calls, market data pulls, hosting, and reproducible reporting.",
    href: "https://buy.stripe.com/4gMeVe1K06DrfaC5dz24001",
    cta: "Contribute $25/mo"
  },
  {
    name: "Sustainer",
    amount: "$100",
    cadence: "monthly",
    description: "Meaningful recurring funding that helps cover future benchmark rounds and audit infrastructure.",
    href: "https://buy.stripe.com/14AdRa88oge15A2gWh24002",
    cta: "Contribute $100/mo"
  },
  {
    name: "Patron",
    amount: "$1,000",
    cadence: "monthly",
    description:
      "Major recurring funding for public benchmark infrastructure. Patron contributions do not influence methodology, model selection, scoring, timing, or results.",
    href: "https://buy.stripe.com/4gM7sM0FWaTH8MecG124003",
    cta: "Become a Patron",
    featured: true
  }
];

export const oneTimeContributionTiers: ContributionTier[] = [
  {
    name: "One-time",
    amount: "$25",
    cadence: "one-time",
    description: "A simple one-time contribution toward public benchmark operations.",
    href: "https://buy.stripe.com/cNi3cw74ke5T3rU7lH24004",
    cta: "Contribute $25"
  },
  {
    name: "One-time",
    amount: "$100",
    cadence: "one-time",
    description: "Helps offset model calls, generated reports, and public site infrastructure.",
    href: "https://buy.stripe.com/fZufZi60g0f3e6ygWh24005",
    cta: "Contribute $100"
  },
  {
    name: "One-time",
    amount: "$250",
    cadence: "one-time",
    description: "Funds a larger share of the data, audit, and reporting work behind public rounds.",
    href: "https://buy.stripe.com/14A5kEewMge10fI49v24006",
    cta: "Contribute $250"
  },
  {
    name: "One-time",
    amount: "$1,000",
    cadence: "one-time",
    description: "A substantial one-time contribution for keeping CapitalBench public and reproducible.",
    href: "https://buy.stripe.com/aFa5kE60gge16E6fSd24007",
    cta: "Contribute $1,000"
  },
  {
    name: "Choose amount",
    amount: "Custom",
    cadence: "one-time",
    description: "Choose a one-time amount through Stripe. Custom recurring amounts are not used for monthly contributions.",
    href: "https://buy.stripe.com/00wfZidsIge15A25dz24008",
    cta: "Choose amount"
  }
];

export const fundingUses = [
  "Model API calls for official and non-official validation runs",
  "Market data used to freeze inputs and score resolved rounds",
  "Cloudflare, Supabase, storage, and deployment infrastructure",
  "Audit hashes, validation checks, public reports, and documentation",
  "Methodology improvements that keep official and stability results separate"
];

