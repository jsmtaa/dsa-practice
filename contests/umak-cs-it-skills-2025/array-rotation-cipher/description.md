# Array Rotation Cipher

#### Description

You are given an array of integers representing valid ASCII values. You must apply a sequence of rotation operations to the array, then extract a hidden message based on prime indices.

---

#### Rotation Rules

Each operation is defined as `(direction, k)`:

* `'L'` (left rotation): shift the array to the left by `k` positions
* `'R'` (right rotation): shift the array to the right by `k` positions

All rotations are applied **sequentially in the given order**.

Rotation is **circular**:

* Elements that go out on one side reappear on the other

---

#### Hidden Message Rule

After applying all rotations:

1. Use **0-based indexing**
2. Identify all indices that are **prime numbers**
   (i.e., 2, 3, 5, 7, 11, …)
3. Extract the elements at those indices
4. Convert each value to its corresponding ASCII character
5. Concatenate them to form the hidden message

---

#### Input

* First line: Integer `N` (5 ≤ N ≤ 100) — size of the array
* Second line: `N` space-separated integers (32 ≤ arr[i] ≤ 126)
* Third line: Integer `M` (1 ≤ M ≤ 20) — number of operations
* Next `M` lines:

  * A character `'L'` or `'R'`
  * An integer `k` (1 ≤ k ≤ N)

---

#### Output

* First line:

  ```
  Final array: <space-separated rotated array>
  ```
* Second line:

  ```
  Hidden message: <decoded string>
  ```

---

#### Notes

* Apply **all rotations exactly as given**
* Use **modulo when rotating**: `k = k % N`
* Prime indices are based on **index positions**, not values
* The hidden message length depends on how many prime indices exist within `[0, N-1]`

---

#### Example

Input:

```
7
72 101 108 108 111 33 65
1
R 2
```

Process:

* After `R 2` → `[33, 65, 72, 101, 108, 108, 111]`
* Prime indices: `2, 3, 5`
* Values: `72, 101, 108` → `"Hel"`

Output:

```
Final array: 33 65 72 101 108 108 111
Hidden message: Hel
```
