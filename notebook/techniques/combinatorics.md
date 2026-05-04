---
status: unlearned
day: 17
invariants:
  - invariant-optimal-substructure
---

# Combinatorics

## Core Idea
Count combinations, permutations, and arrangements using mathematical formulas and modular arithmetic. Python 3.8+ has `math.comb()` for fast binomial coefficient calculation.

## When to Use
- Counting problems: "how many ways to arrange X"
- Probability calculations in contests
- Modular arithmetic for large factorials
- Catalan number problems

## Template Code
```python
from math import comb, factorial

# Built-in: Python 3.8+
def combinations_builtin(n, k):
    return comb(n, k)

# Manual calculation with modular arithmetic
MOD = 10**9 + 7

def factorial_mod(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)  # Fermat's little theorem

def comb_mod(n, k):
    if k > n or k < 0:
        return 0
    numerator = factorial_mod(n)
    denominator = (factorial_mod(k) * factorial_mod(n - k)) % MOD
    return (numerator * mod_inverse(denominator, MOD)) % MOD

# Catalan number
def catalan(n):
    return comb_mod(2 * n, n) - comb_mod(2 * n, n + 1)

# Modular exponentiation
def power_mod(base, exp, mod):
    return pow(base, exp, mod)
```

## Linked Invariants
- [[invariant-optimal-substructure]]

## Linked Problems
(Day 17: counting problems, Catalan sequences, modular exponentiation, etc.)

## Common Pitfalls
- Overflow: always use modular arithmetic for large answers
- Fermat's little theorem (mod inverse): only works if mod is prime
- Confusing nCk with nPk (combinations vs. permutations)
- Off-by-one in Catalan or other formula applications
