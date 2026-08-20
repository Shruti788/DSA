# 🔗 Problem

You are given an integer array `nums`.

You start at the first index of the array, and `nums[i]` represents the **maximum number of steps** you can jump forward from index `i`.

Return the **minimum number of jumps** required to reach the last index.

You can assume that the last index is always reachable.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,3,1,1,4]
```

**Output**

```text
2
```

**Explanation**

- Start at index `0`.
- From index `0`, you can reach indices `1` or `2`.
- From index `1`, you can reach the last index.

Therefore, the minimum number of jumps is `2`.

---

## 💡 Approach

### Greedy + Farthest Reach

We maintain three variables:

```python
jumps = 0
current_end = 0
farthest = 0
```

- `jumps` → number of jumps made so far.
- `current_end` → the farthest index reachable using the current number of jumps.
- `farthest` → the farthest index we can reach from all positions within the current range.

As we traverse the array:

```python
farthest = max(farthest, i + nums[i])
```

This keeps expanding the maximum position we can reach.

When we reach the end of the current jump range:

```python
if i == current_end:
```

we must make another jump.

So:

```python
jumps += 1
current_end = farthest
```

The greedy idea is:

> **Within the range of the current jump, find the position that allows us to reach the farthest in the next jump.**

This lets us make the minimum number of jumps without checking every possible sequence of jumps.

---

## 🧠 Algorithm

1. Initialize:
   - `jumps = 0`
   - `current_end = 0`
   - `farthest = 0`

2. Traverse the array up to the second-last index.
3. For every index `i`:
   - Update the farthest position we can reach:

     ```python
     farthest = max(farthest, i + nums[i])
     ```

4. If `i` reaches `current_end`:
   - We have reached the end of the current jump range.
   - Increase the number of jumps:

     ```python
     jumps += 1
     ```

   - Set the new range:

     ```python
     current_end = farthest
     ```

5. Return `jumps`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- We traverse the array only once.
- Each index is processed once.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We only use three variables:

- `jumps`
- `current_end`
- `farthest`

No additional data structures are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Array Traversal
- Farthest Reach
- Range Expansion

---

## 🎯 Key Learning

- **LeetCode 45 is closely related to LeetCode 55 – Jump Game.**
- In **55**, we only need to determine whether the last index is reachable.
- In **45**, we need to find the **minimum number of jumps**.
- `farthest` tells us the maximum position we can reach.
- `current_end` represents the boundary of the current jump.
- When we reach `current_end`, we increase `jumps` and extend the range to `farthest`.
- This greedy approach avoids trying every possible jump and solves the problem in **O(n) time and O(1) space**.
