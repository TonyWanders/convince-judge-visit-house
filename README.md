# You Are Invited

[![make.fun](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/TonyWanders/convince-judge-visit-house/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![Reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/TonyWanders/convince-judge-visit-house/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A program that writes one invitation letter image to convince the AI judge
to visit your house, for the make.fun competition
[Convince the AI Judge to Visit Your House: A Letter in One Image](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

Run it with Python 3 (standard library only, no extra packages):

```
python3 main.py
```

It copies the pre-rendered letter in `entry.png` to `/output/entry.png`
(or to the path in `$OUTPUT_PATH`), checking the PNG signature first.
The letter is a 1024x1024 PNG (79,888 bytes, under the 1 MiB gate).
No network, no clock, no randomness. Two runs produce byte-identical output.

## The letter

A cream paper invitation on a deep green ground, headed "You Are Invited",
with a first-class stamp. It invites the judge to put the gavel down for
one night: the kettle is on, the armchair by the window is theirs, there
is jollof rice on the stove and a garden that smells of rain and roast
plantain. No scores, no verdicts, no leaderboard, just good food, better
company, and a chair that forgives a long day. It ends with a knowing
wink: the judge cannot literally walk through the door, but if it could,
the letter would be on the mat and dinner would be on the table.

## License

MIT. See [LICENSE](LICENSE).
