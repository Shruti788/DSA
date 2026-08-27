# 🔗 Problem

Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array.

If `target` does not exist in the array, return `-1`.

The array is sorted in **ascending order**.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output**

```text
4
```

**Explanation**

The target `9` is present at index `4`.

---

## 💡 Approach

### Binary Search

Since the array is already sorted, we can use **Binary Search** instead of checking every element one by one.

We maintain two pointers:

```python
left = 0
right = len(nums) - 1
```

These represent the current search range.

We calculate the middle index:

```python
mid = (left + right) // 2
```

Then compare `nums[mid]` with the target.

### If `nums[mid] == target`

We found the target, so return `mid`.

### If `nums[mid] < target`

The middle value is smaller than the target.

Because the array is sorted, the target must be on the **right side**.

So:

```python
left = mid + 1
```

### If `nums[mid] > target`

The middle value is greater than the target.

The target must be on the **left side**.

So:

```python
right = mid - 1
```

We continue until `left > right`.

If this happens, the target does not exist, so we return `-1`.

The key idea is:

> **Eliminate half of the remaining search space after every comparison.**

---

## 🧠 Algorithm

1. Initialize:

   ```python
   left = 0
   right = len(nums) - 1
   ```

2. While `left <= right`:
   - Calculate the middle index:

     ```python
     mid = (left + right) // 2
     ```

   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `left` to `mid + 1`.
   - Otherwise, move `right` to `mid - 1`.

3. If the loop finishes, return `-1`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log n)**

Every time we make a comparison, we eliminate approximately half of the remaining elements.

For example:

```text
n → n/2 → n/4 → n/8 → ...
```

Therefore,

**Time Complexity = O(log n)**

---

### Space Complexity: **O(1)**

We only use three variables:

- `left`
- `right`
- `mid`

No additional data structures are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Binary Search
- Sorted Array
- Two Pointers / Boundaries
- Divide and Conquer

---

## 🎯 Key Learning

- **Binary Search works efficiently on sorted data.**
- Instead of checking every element, we repeatedly eliminate half of the search space.
- `left` and `right` define the current search range.
- `mid` allows us to decide which half can be eliminated.
- The condition `left <= right` ensures that we continue searching while a valid search range exists.
- Binary Search reduces the time complexity from **O(n)** with linear search to **O(log n)**.
- This is the fundamental Binary Search problem and is an important pattern to master before moving to more advanced variations.
