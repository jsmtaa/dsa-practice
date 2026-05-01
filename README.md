# dsa-practice

Personal practice repository for data structures and algorithms problems. This repo serves as the main container for all DSA practice across devices.

## Structure

- `problems/leetcode/` — LeetCode solutions, one file per problem (`lc_XXXX.py`)
- `problems/codeforces/` — Codeforces solutions
- `patterns/` — pattern guides with explanations and examples
- `contests/` — timed contest problems organized by session
- `schedule.md` — spaced repetition review tracker

## Method

Problems are organized by pattern. Each solution file opens with a standard header:

```
PROBLEM   : <name>
DIFFICULTY: <easy | medium | hard>
PATTERN   : <pattern>
TRIGGER   : <keywords that hint at this pattern>
INTUITION : <plain-English explanation of the approach>
```

After solving a problem, it is logged in `schedule.md` with a mastery score and a calculated next-review date. Review intervals increase as mastery improves (1d → 2d → 4d → 7d → 14d).
