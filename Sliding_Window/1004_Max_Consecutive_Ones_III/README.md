## 🔗 Problem

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` zeros.

In other words, find the **longest contiguous subarray containing at most `k` zeros**.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

**Output**

```text
6
```

---

### Example 2

**Input**

```text
nums = [0,0,1,1,1,0,0]
k = 0
```

**Output**

```text
3
```

---

## 💡 Approach

This problem can be solved using the **Sliding Window** technique.

We maintain a window between two pointers:

```text
left
  ↓
[  current window  ]
                  ↑
                right
```

The window is valid when it contains **at most `k` zeros**.

We keep track of the number of zeros inside the current window using:

```python
zero_count
```

### Steps

1. Start with:
   - `left = 0`
   - `zero_count = 0`
   - `max_length = 0`

2. Move `right` through the array.

3. Whenever `nums[right]` is `0`, increase `zero_count`.

4. If the number of zeros becomes greater than `k`, the window becomes invalid:

```python
while zero_count > k:
```

5. Move `left` forward to shrink the window.

6. If the element leaving the window is `0`, decrease `zero_count`.

7. Once the window is valid again, calculate its length:

```python
right - left + 1
```

8. Keep the maximum window length.

---

## ⏱️ Complexity

### Time Complexity

```text
O(n)
```

The `right` pointer moves from left to right once, and the `left` pointer also moves from left to right at most once.

Therefore, the overall complexity is `O(n)`.

### Space Complexity

```text
O(1)
```

We only use a few variables regardless of the size of the input.

---

## 🧠 Key Pattern

This is a **Variable-Size Sliding Window** problem.

---
