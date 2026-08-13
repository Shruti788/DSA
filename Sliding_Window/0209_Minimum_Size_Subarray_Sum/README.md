## 🔗 Problem

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

---

## 📝 Example

### Example 1

**Input**

```text
target = 7
nums = [2,3,1,2,4,3]
```

**Output**

```text
2
```

---

## 💡 Approach — Sliding Window

We use a **variable-size sliding window** with two pointers:

- `left` → start of the window
- `right` → end of the window

We expand the window using `right`.

When the window sum becomes greater than or equal to `target`, we shrink the window from the left to find the minimum length.

---

## ⏱ Complexity Analysis

### Time Complexity: O(n)

Each element is added to the window once and removed from the window at most once.

### Space Complexity: O(1)

Only a few variables are used.

---

## 📚 Concepts Used

- Sliding Window
- Two Pointers
- Variable-Size Window
- Array Traversal

---

## 🎯 Key Learning

The important pattern is:

```text
Expand → condition becomes valid → Shrink → find minimum
```

Because all numbers are positive, removing an element from the left always decreases the window sum.

---

## 🏷️ Tags

`Array` `Sliding Window` `Two Pointers`
