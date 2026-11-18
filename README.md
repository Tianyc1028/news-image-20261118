[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Tianyc1028/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Tianyc1028/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — 18 November 2026

A one-page newspaper poster that sums up the world news of Wednesday
18 November 2026 in a single image. An AI judge compares entries pairwise;
the 50 best share $250.

## The image

`entry.png` (1024×1024, drawn with Pillow from real reporting) leads with
the Gulf escalation — US jets struck a missile site on Qeshm Island and
Iran fired drones at US bases in Bahrain and Kuwait — beside a schematic
map of the Strait of Hormuz. Four more stories cover the other regions
and fields of the day:

- **Ukraine** — the Kerch Bridge to Crimea partly collapses after a
  second day of Ukrainian drone and missile strikes.
- **China** — Xi Jinping and Vladimir Putin meet in Shenzhen, a day
  before a planned three-way summit with Donald Trump.
- **United States** — Mary Peltola wins Alaska; Democrats take a
  projected 56–44 Senate majority.
- **Health** — the Ebola outbreak in DR Congo more than doubles:
  over 11,000 cases and 5,400 deaths.

An "Also today" strip adds the Russian military plane crash in Siberia
(19 dead), Nvidia's record quarterly revenue, Category 5 Cyclone Xavier
in the Cook Islands, a 6.0 quake in Papua New Guinea, and Cambridge
Dictionary's word of the year, "Human". Sources are listed on the
poster (AP · Reuters · AFP · Just Security).

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`, byte for byte, so both grading runs write identical
bytes. It runs with no network.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
