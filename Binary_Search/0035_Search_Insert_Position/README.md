# 🔗 Problem

Given a sorted array of distinct integers `nums` and an integer `target`, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

The algorithm must run in **O(log n)** time.

---

## 📝 Example 1

**Input**

```text
nums = [1,3,5,6]
target = 5
```

**Output**

```text
2
```

**Explanation**

The target `5` is already present at index `2`.

---

## 💡 Approach

### Binary Search

Since the array is sorted, we can use **Binary Search** to find the target or determine its correct insertion position.

We initialize:

```python
left = 0
right = len(nums) - 1
```

Then repeatedly calculate the middle index:

```python
mid = (left + right) // 2
```

We compare `nums[mid]` with `target`.

### If `nums[mid] == target`

The target is found, so we return `mid`.

### If `nums[mid] < target`

The target must be somewhere to the **right**:

```python
left = mid + 1
```

### If `nums[mid] > target`

The target must be somewhere to the **left**:

```python
right = mid - 1
```

When the loop ends:

```python
left > right
```

At this point, `left` represents the correct position where the target should be inserted.

Therefore, we return:

```python
return left
```

The key idea is:

> **When Binary Search finishes without finding the target, `left` points to the target's correct insertion position.**

---

## 🧠 Algorithm

1. Initialize:

   ```python
   left = 0
   right = len(nums) - 1
   ```

2. While `left <= right`:
   - Calculate `mid`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `left` to `mid + 1`.
   - Otherwise, move `right` to `mid - 1`.

3. If the target is not found, return `left`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log n)**

Each iteration eliminates approximately half of the remaining search space.

Therefore,

**Time Complexity = O(log n)**

---

### Space Complexity: **O(1)**

We only use:

- `left`
- `right`
- `mid`

No additional data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Binary Search
- Sorted Array
- Search Space Reduction
- Insertion Position

---

## 🎯 Key Learning

- Binary Search can be used not only to **find an element**, but also to find its **correct position**.
- If the target is found, return `mid`.
- If the target is not found, `left` naturally becomes the correct insertion position.
- The important difference from **LeetCode 704 – Binary Search** is the final condition:
  - **704:** return `-1` if the target is not found.
  - **35:** return `left` because we need the insertion position.

- This problem is a fundamental example of using Binary Search to find a **boundary position**.
- The solution runs in **O(log n) time and O(1) space**.
