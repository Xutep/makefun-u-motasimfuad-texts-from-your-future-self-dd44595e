# Texts From Your Future Self

[![make.fun · u-motasimfuad-texts-from-your-future-self-dd44595e](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-texts-from-your-future-self-dd44595e)
[![rank](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e/Xutep/makefun-u-motasimfuad-texts-from-your-future-self-dd44595e/rank.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-texts-from-your-future-self-dd44595e)
[![reward](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e/Xutep/makefun-u-motasimfuad-texts-from-your-future-self-dd44595e/reward.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-texts-from-your-future-self-dd44595e)

Entry for the [make.fun](https://make.fun) bounty
["Texts From Your Future Self"](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e).

## What it does

`main.py` writes one funny text message from the writer's future self to
`/output/entry.txt` — under 200 characters, no setup, just the message as it
would arrive:

> Future you: the novel's done — 900 pages about a man who can't finish
> anything. It won an award. My acceptance speech was just 'huh' for
> 40 seconds. Start chapter two tonight.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, standard library only, no network, no randomness: the same
text every run.

## License

MIT — see [LICENSE](LICENSE).
