# Texts From Your Future Self

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)
[![competition](https://make.fun/badge/competition/u-motasimfuad-texts-from-your-future-self-dd44595e.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)

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
