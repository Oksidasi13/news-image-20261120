# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Oksidasi13/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Oksidasi13/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

The world's news of Friday 20 November 2026, summed up in one image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## The image

A newspaper infographic drawn by hand with Python PIL and DejaVu
fonts: a header naming the day, then six story cards in a 2-by-3
grid. `draw.py` is the drawing program; `entry.png` is the image
it produces.

## The six stories

The picture was first drawn early on Friday (07:00 WIB), then
redrawn on Friday night (19:30 WIB) once the day's two moving
stories had settled: Cyclone Akvan came ashore in the morning and
weakened, and the COP31 draft dropped its fossil-fuel wording and
its $120bn adaptation goal with no final deal in sight. The GTA 6
launch-day figure was also refreshed to Sensor Tower's end-of-day
estimate. The other three stories were checked again against fresh
sources on Friday night and left as first written. Every story was
checked against at least two independent news sources.

1. **Diplomacy — Washington / Iran.** President Trump says he is
   in "no rush" over new strikes on Iran and will "see what happens
   after January 1", putting any decision into 2027. He said it to
   Reuters, Fox News and Axios/News 12 while flying home from
   China. Sources: Reuters, The Times of India, Axios.
2. **Weather — Odisha, India.** Cyclone Akvan comes ashore near
   Gopalpur on Friday morning — landfall done by 11:20 IST, winds
   70–80 km/h gusting to 90 — and weakens to a deep depression,
   after roughly 300,000 people were moved to shelters. No major
   damage or loss of life has been reported in Odisha so far.
   Sources: The Hindu BusinessLine, Reuters/PTI, India
   Meteorological Department, Sambad English.
3. **Justice — The Hague.** The International Court of Justice
   rules 9–6 that Myanmar committed genocide against the Rohingya
   in its 2017 crackdown, which killed about 10,000 people, and
   orders reparations. The ruling came down on Thursday 19
   November and led Friday's world news. Sources: BBC, Reuters,
   The Guardian.
4. **Climate — Antalya, Turkey.** COP31 hits its scheduled closing
   day on Friday with no final deal: the latest draft drops every
   mention of fossil fuels and the $120bn adaptation-finance
   target, and the talks may spill into the weekend. Sources:
   Reuters, CNN, phys.org/AFP, AsiaToday.
5. **Space.** NASA confirms Voyager 1 is the first spacecraft to
   fly more than a light-day from Earth — around 26 billion km —
   after 49 years in space. It crossed the mark on Wednesday, and
   its signal took a day to reach Earth. Sources: Reuters, AP,
   Marketscreener.
6. **Entertainment.** GTA 6 takes an estimated $2.36bn by the end
   of its launch day, from about 24.6 million copies sold — the
   biggest game launch ever, passing the entire $1.8bn worldwide
   box-office run of Christopher Nolan's The Odyssey (a Sensor
   Tower estimate, not an official figure; its Thursday-morning
   reading was $1.84bn from 19.1 million copies). Sources:
   Reuters, Notebookcheck, GameSpot, 80.lv.

## Build

`python3 draw.py` redraws `entry.png` (a 1024x1024 PNG) from the
story texts; `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`
copies it to `out/entry.png`.
