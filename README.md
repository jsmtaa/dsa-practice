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

---

## Obsidian Vault — Competitive Programming Knowledge Graph

An interconnected Obsidian vault for **active recall training** on competitive programming patterns. The vault encodes invariants (core properties underlying techniques) as first-class nodes, with techniques and daily lessons linking to them. This forms a knowledge graph optimized for DFS/BFS-style traversal and spaced repetition.

### Vault Structure

**Location**: `notebook/` (73 interconnected notes)

- **`moc/`** (4 Maps of Content — entry points)
  - `invariants.md` — Lists all 6 core invariants with links to exploiting techniques
  - `techniques.md` — All 32 techniques grouped by invariant
  - `data-structures.md` — 9 core data structures (linear, hierarchical, network)
  - `review-plan.md` — 22-day learning schedule with daily targets

- **`invariants/`** (6 core patterns)
  - `invariant-monotonicity` — Exploit ordered/sorted structure (2 Pointers, Sliding Window, Binary Search)
  - `invariant-optimal-substructure` — Build from subproblem solutions (DP, Tree DP, Recursion)
  - `invariant-overlapping-subproblems` — Cache to avoid recalculation (DP variants)
  - `invariant-state-space-search` — Explore state space (BFS, DFS, Backtracking, Topological Sort)
  - `invariant-range-queries` — Fast aggregates over intervals (Prefix Sum, Segment Tree, Fenwick Tree)
  - `invariant-greedy-choice-property` — Local optimum → global optimum (Greedy Algorithms)

- **`techniques/`** (32 algorithm techniques)
  - #learned: Two Pointers, Sliding Window, Dynamic Programming (Intro)
  - #partial: Sorting + Binary Search, Stacks/Queues, Greedy, Linked Lists, DP (1D)
  - #unlearned: Prefix Sum, Hashing, Recursion/Backtracking, Monotonic Stack, Tree Traversals, BFS, DFS, Topological Sort, Union-Find, DP (2D), LIS, Dijkstra, Bellman-Ford, Tree DP, LCA, Segment Tree, Fenwick Tree (BIT), String Hashing, KMP, Trie, Bitmask DP, Combinatorics

- **`data-structures/`** (9 core data structures)
  - Array, Linked List, Stack, Queue, Deque, Hash Map, Tree, Heap, Graph
  - Each includes complexity analysis, Python idiom, and linked techniques

- **`daily-plan/`** (22-day competitive programming roadmap)
  - Days 01–04: Core patterns (Two Pointers, Prefix Sum, Binary Search, Backtracking)
  - Days 05–10: Data structures (Stacks/Queues, Greedy, Trees, Graphs, Union-Find, DP 1D)
  - Days 11–17: Advanced patterns (DP 2D, Dijkstra, Tree DP, Range Queries, Strings, Bitmask)
  - Days 18–22: Mock contests and final polish

### How to Use

**Start here**: Open `moc/invariants.md` in Obsidian.

**Learning flow**:
1. Pick an invariant (e.g., [[invariant-monotonicity]])
2. See which techniques exploit it
3. Navigate to a technique (e.g., [[two-pointers|Two Pointers]])
4. Study the core idea, template, and common pitfalls
5. Solve linked problems (via daily-plan references)
6. Update status tags (#unlearned → #partial → #learned)

**Spaced repetition**: Use the 7-day BFS review schedule in `VAULT_REPORT.md` for active recall. Revisit invariants every 2–3 days; techniques as you progress.

**Contest prep**: Follow the 22-day battle plan via `daily-plan/day-01.md` through `day-22.md`. Days 18–22 focus on mock contests and reviewing editorials (80% of learning).

### Key Features

- **Knowledge graph**: 73 notes with 100+ wikilinks; no orphan notes
- **Linking rules**:
  - Every technique links to ≥1 invariant
  - Every invariant links to ≥2 techniques
  - All notes are reachable via wikilinks
- **Status tags**: #learned (confident), #partial (practice needed), #unlearned (not ready)
- **Critical corrections**: BFS uses **queues**, DFS uses **stacks** — emphasized throughout
- **Template code**: Each technique includes Python-specific, competition-ready implementations

### 22-Day Learning Plan

This is the authoritative competitive programming roadmap (source: `battle plan.md`).

- **Phase 1 (Days 1–4)**: Core patterns — re-learn fast (3x faster than first-time)
- **Phase 2 (Days 5–10)**: Data structures — crack Medium problems consistently
- **Phase 3 (Days 11–17)**: Hard patterns — pattern recognition for Extreme problems
- **Phase 4 (Days 18–20)**: Mock contests — 80% of growth from editorial review
- **Phase 5 (Days 21–22)**: Polish — revisit weak spots, finalize templates, sleep well

Each day targets 6–10 problems. After Day 4, aim for confident Easy solving and Medium attempts. After Day 10, crack Mediums. After Day 17, pattern recognize on Hard problems.

### Color Tag Suggestions

For use in Obsidian:
- `#learned` → 🟢 Green (confident, ready to use)
- `#partial` → 🟡 Yellow (needs practice, getting there)
- `#unlearned` → 🔴 Red (not ready yet, priority to learn)
- `#core` → 🔵 Blue (foundational, fundamental concept)
- `[phase:foundational]` → 🔴 Red (Days 1–4)
- `[phase:core]` → 🟠 Orange (Days 5–10)
- `[phase:advanced]` → 🟡 Yellow (Days 11–17)
- `[phase:application]` → 🟢 Green (Days 18–22)

### Verification Report

See `notebook/VAULT_REPORT.md` for:
- File count by folder (73 total)
- Orphan note detection (none — all linked)
- Linking rule validation (all pass ✅)
- Critical corrections applied (BFS/DFS confusion resolved)
- 7-day BFS review schedule for active recall
