# MOC — Data Structures

Core data structures and their roles in competitive programming.

## Linear Structures
- [[Array]] — Random access, O(1); insertion/deletion at middle is O(n)
- [[Linked List]] — O(1) insertion/deletion at known position; no random access
- [[Stack]] — LIFO; powers DFS and expression parsing
- [[Queue]] — FIFO; powers BFS and scheduling
- [[Deque]] — Both ends; enables sliding window tricks

## Key-Value Structures
- [[Hash Map]] — Fast O(1) lookup and frequency counting

## Hierarchical Structures
- [[Tree]] — Binary tree, BST; basis for traversals and tree DP
- [[Heap]] — Min/max extraction in O(log n); priority queues

## Network Structures
- [[Graph]] — Adjacency list; foundation for pathfinding (BFS, Dijkstra, etc.)

---

## How to Choose
- Need fast lookup? → Hash Map
- Need both ends? → Deque
- Need to always remove minimum? → Heap
- Need to explore structure level-by-level? → Queue (BFS)
- Need to go deep, backtrack? → Stack (DFS)
- Need sorted dynamic data? → Tree (BST)
- Need connections/paths? → Graph

Next: [[review-plan]] for your day-by-day learning schedule
