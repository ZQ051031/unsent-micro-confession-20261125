# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ZQ051031/unsent-micro-confession-20261125/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ZQ051031/unsent-micro-confession-20261125/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

One micro-confession in exactly two parts: a `To:` line naming who it was
meant for, and the unsent message itself, one line written exactly as it
was typed, with no explanation after it.

## The entry

> To: the friend I ghosted after your dad's funeral
>
> I typed "I'm sorry I wasn't there" six times and deleted it every time because sorry felt too small and too late at once.

The confession is 172 characters in total (171 without the trailing
newline): the `To:` line is 49 characters and the unsent message is
121 characters, one line, well inside the competition's 260-character
gate and its 200-character message limit. The addressee and the message
need each other — the apology only makes sense to the friend who was
ghosted after the funeral — and the reason it stayed in drafts is felt
in the words themselves: sorry felt too small and too late at once, so
the message was typed six times and deleted every time.

## How it works

`main.py` (Python 3 standard library only, no network) deterministically
writes the entry to `/output/entry.txt`. It checks its own output
against the gate before writing: 1–260 characters total, exactly two
lines, a `To:` first line, and a message line of at most 200 characters.
Running it twice produces byte-identical output.

Run it with:

```sh
python3 main.py
```

Then check the result with:

```sh
cat /output/entry.txt
sha256sum /output/entry.txt
```

## Competition

[Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) on make.fun — entries close November 26, 2026, 09:30 CST.

## License

MIT — see [LICENSE](LICENSE).
