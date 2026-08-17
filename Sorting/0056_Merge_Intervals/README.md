## 🔗 Problem

You are given an array of intervals where `intervals[i] = [starti, endi]`.

Merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## 📝 Example

### Example 1

**Input**

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output**

```text
[[1,6],[8,10],[15,18]]
```

---

### Example 2

**Input**

```text
intervals = [[1,4],[4,5]]
```

**Output**

```text
[[1,5]]
```

---

## 💡 Approach

### Sorting + Greedy

First, sort the intervals based on their starting values.

For example:

```text
[[8,10],[1,3],[2,6],[15,18]]
```

becomes:

```text
[[1,3],[2,6],[8,10],[15,18]]
```

After sorting, we can compare each interval with the last interval in our `result`.

For each `current` interval:

- Get the last interval from `result`.
- Check whether the current interval overlaps with the last interval.
- Two intervals overlap when:

```python
current[0] <= last[1]
```

- If they overlap, merge them by keeping:
  - The existing starting point.
  - The larger ending point.

This is done using:

```python
last[1] = max(last[1], current[1])
```

For example:

```text
last    = [1,6]
current = [2,8]
```

Since `2 <= 6`, they overlap.

The merged interval becomes:

```text
[1,8]
```

If the intervals do not overlap, add the current interval to `result`.

---

## 🧠 Algorithm

1. Sort all intervals by their starting value.
2. Initialize `result` with the first interval.
3. Traverse the remaining intervals.
4. Store the last merged interval in `last`.
5. Check if `current[0] <= last[1]`.
6. If they overlap:
   - Update `last[1]` to the larger ending value.

7. If they do not overlap:
   - Add `current` to `result`.

8. Return `result`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n)**

- Sorting the intervals takes **O(n log n)**.
- Traversing the intervals takes **O(n)**.
- Therefore, the overall time complexity is dominated by sorting.

Therefore,

**Time Complexity = O(n log n)**

where:

- **n** = number of intervals.

---

### Space Complexity: **O(n)**

- The `result` array stores the merged intervals.
- In the worst case, none of the intervals overlap, so `result` can contain all `n` intervals.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Sorting
- Greedy Algorithm
- Array Traversal
- Intervals
- Merging Intervals

---
