# Contributing

We accept PRs adding verified free AI tools.

## Requirements

Every new entry **must**:

1. **Actually exist** — URL must resolve and serve content
2. **Be genuinely free** — no credit card required, no "free trial" that expires
3. **Have a meaningful free tier** — not just a 3-day trial or "free" that is unusable

## How to add a tool

1. Add to `data/verified-tools.json` with the correct category
2. Run `python3 .github/scripts/check_links.py` to verify the URL works
3. Update the table in `README.md` under the appropriate category
4. Submit a PR

## Categories

- `ai-chat`, `ai-image`, `ai-video`, `ai-music`, `ai-code`
- `ai-agents`, `ai-search`, `ai-productivity`, `ai-local`, `ai-privacy`

## What NOT to submit

- Paid-only tools hiding behind "free trial"
- Tools requiring credit card for signup (⚠️ is for exceptions only)
- Dead or parked domains
- AI-generated tool entries that don't exist

## Verification

All tools are verified weekly by the link checker workflow.
