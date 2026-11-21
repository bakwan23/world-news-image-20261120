# The World in One Day — Friday 20 November 2026

Entry for the make.fun bounty **"Sum up 20 November's world news in one image"**
(`make.fun/bounty/news-image-20261120`). $250 in USDC, 50 places paid
(1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3).
**Deadline: Sunday 22 November 2026, 00:00 UTC (07:00 WIB).**

## What it is

A one-page newspaper front page (`entry.png`, 1024×1024, ~130 KB) summing up
Friday 20 November 2026:

- **Top story:** the International Court of Justice finds Myanmar committed
  genocide against the Rohingya — the first such finding against a state.
- Trump, Xi and Putin hold their first three-way summit in Shenzhen and issue
  a joint peace declaration.
- Markets tumble: Nikkei −4.8%, S&P 500 enters correction as AI stocks sell
  off after Anthropic's Nasdaq debut.
- Houthi missiles damage a Riyadh skyscraper; Kenya discharges its last Ebola
  patient (37 days after the first case); Ukraine hits the Crimean Bridge span.
- Also: Trump threatens penalties for US tech firms building data centres
  abroad; GTA VI launches; French police sentenced over the racist beating of
  a music producer.
- Markets at the close: S&P 500 7,175.83 (−2.02%), Nasdaq 23,879.20 (−2.25%),
  Dow 49,097.06 (−2.19%), Gold $3,530.75 (−2.58%).

News sources: oneturn.news (20 Nov 2026 daily brief), The PostHole afternoon
edition (20 Nov 2026), Standard Topic / NEXA world archive for 20 Nov 2026,
and the make.fun bounty page itself.

## How it works

`main.py` copies `entry.png` to `/output/entry.png`. No network, no
randomness, no clock — both runs write byte-identical output, as the bounty
requires. Rebuild the image any time with `python3 build_image.py`
(needs Pillow; uses DejaVu fonts).

## How to submit (from a phone)

1. Create a free GitHub account at github.com (email only, no card).
2. Create a new **public** repository (e.g. `news-image-20261120`) and upload
   these files: `entry.png`, `main.py`, `LICENSE`, `README.md`,
   `TRANSCRIPT.md`. The repo must be created after the bounty opened
   (20 Nov 2026 00:00 UTC) — creating it today satisfies this.
3. Open `make.fun/bounty/news-image-20261120`, enter the bounty, link the
   repository (or send a source bundle) and upload `TRANSCRIPT.md` with the
   submission.
4. If the entry places in the top 50, claim the USDC from the bounty's escrow
   to a Solana wallet. Never share a private key or seed phrase with anyone.

## Files

- `entry.png` — the entry image (1024×1024 PNG, under 1 MiB).
- `main.py` — the entry program (Python 3.13).
- `build_image.py` — the script that drew `entry.png`.
- `LICENSE` — MIT.
- `TRANSCRIPT.md` — build log of the agent session that made this entry.
