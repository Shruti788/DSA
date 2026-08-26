# 🔗 Problem

You are given an array of intervals where:

```text
intervals[i] = [start_i, end_i]
```

Return the **minimum number of intervals that must be removed** so that the remaining intervals do not overlap.

---

## 📝 Example

### Example 1

**Input**

```text
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

**Output**

```text
1
```

**Explanation**

We can remove `[1,3]`.

The remaining intervals:

```text
[1,2], [2,3], [3,4]
```

do not overlap.

## Therefore, we only need to remove **1 interval**.

## 💡 Approach

### Greedy + Sorting

First, sort the intervals by their **ending point**:

```python
intervals.sort(key=lambda x: x[1])
```

Then we keep track of the ending point of the last interval that we decided to keep:

```python
end_point = intervals[0][1]
```

For every following interval:

- If its starting point is **less than** `end_point`, the intervals overlap.
- Therefore, we remove the current interval:

  ```python
  count += 1
  ```

- Otherwise, there is no overlap, so we keep the interval and update:

  ```python
  end_point = intervals[i][1]
  ```

The greedy idea is:

> **Always keep the interval with the earliest ending point.**

An interval that ends earlier leaves more room for future intervals, allowing us to keep as many intervals as possible.

---

## 🧠 Algorithm

1. Sort `intervals` by their ending point.
2. Initialize:

   ```python
   count = 0
   ```

3. Set `end_point` to the ending point of the first interval.
4. Traverse the remaining intervals.
5. For each interval:
   - If `intervals[i][0] < end_point`:
     - The current interval overlaps.
     - Increment `count`.

   - Otherwise:
     - Keep the interval.
     - Update `end_point`.

6. Return `count`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n)**

- Sorting the intervals takes **O(n log n)**.
- Traversing the intervals takes **O(n)**.

Therefore,

**Time Complexity = O(n log n)**

---

### Space Complexity: **O(1)**

Apart from the sorting operation, we only use a few variables:

- `count`
- `end_point`
- `i`

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Intervals
- Array Traversal

---

## 🎯 Key Learning

- For interval problems, sorting by the **ending point** can help reveal a greedy strategy.
- When two intervals overlap, keep the interval that **ends earlier**.
- The interval with the smaller ending point leaves more space for future intervals.
- `count` represents the number of intervals that need to be removed.
- This problem is closely related to **LeetCode 452 – Minimum Number of Arrows to Burst Balloons**, where sorting by ending points also leads to a greedy solution.
- This is a classic **Greedy + Sorting + Intervals** problem with **O(n log n) time**.
