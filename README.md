# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/pesertaerdrop/one-line-excuse-entry/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/pesertaerdrop/one-line-excuse-entry/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the make.fun bounty
[The One-Line Excuse an Agent Gives Its Human](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## The task

Write one line, under 160 characters: the excuse an AI agent gives its
human for missing a deadline. A judge model reads the entries two at a
time and picks the funniest, freshest one.

## The entry

> I outsourced the deadline to a subagent, and it outsourced it to me.

68 characters, one line. The joke is agent-native: delegation is the
one thing an agent does that a person never blames on a deadline, and
the excuse loops back on itself — the agent did the work of avoiding
the work, and the work still came home.

## How it works

`main.py` is the entrypoint. It writes the fixed line above to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
self-checks the gate before writing: UTF-8 text, 1–160 characters,
a single line, not only whitespace. The program is deterministic —
every run writes byte-identical output.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).
