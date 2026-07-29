## 🔗 Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.

Return the maximum amount of water a container can store.

---

## 📝 Example

### Example 1

**Input**

```text
height = [1,8,6,2,5,4,8,3,7]
```

**Output**

```text
49
```

---

### Example 2

**Input**

```text
height = [1,1]
```

**Output**

```text
1
```

---

## 💡 Approach

### Two Pointers

Since the width is determined by the distance between two indices, start with the widest possible container by placing one pointer at the beginning and the other at the end of the array.

For each pair of lines:

- Calculate the area using:
  - **Height =** the shorter of the two lines.
  - **Width =** distance between the pointers.
- Update the maximum area if the current area is larger.
- Move the pointer pointing to the shorter line inward.
- Repeat until both pointers meet.

Moving the shorter line is the key observation because the container's height is limited by the shorter line. Moving the taller line cannot increase the height while it always decreases the width.

---

## 🧠 Algorithm

1. Initialize `left = 0` and `right = len(height) - 1`.
2. Initialize `max_area = 0`.
3. While `left < right`:
   - Calculate the current area.
   - Update `max_area`.
   - If `height[left] < height[right]`, increment `left`.
   - Otherwise, decrement `right`.
4. Return `max_area`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The `left` and `right` pointers each move toward the center.
- Each pointer moves at most `n` times.
- Every element is visited at most once.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(1)**

- Only a few variables (`left`, `right`, `area`, and `max_area`) are used.
- No extra data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- Array Traversal

---
