# 🔗 Problem

Given a positive integer `num`, determine whether it is a **perfect square**.

A perfect square is an integer that can be expressed as the product of an integer with itself.

For example:

```text
4 = 2 × 2
9 = 3 × 3
16 = 4 × 4
```

Return `True` if `num` is a perfect square, otherwise return `False`.

You must solve the problem without using built-in square root functions.

---

## 📝 Example

### Example 1

**Input**

```text
num = 16
```

**Output**

```text
true
```

**Explanation**

```text
4 × 4 = 16
```

Therefore, `16` is a perfect square.

---

## 💡 Approach

### Binary Search

We can use **Binary Search** to efficiently search for an integer whose square equals `num`.

We initialize:

```python
left = 1
right = num
```

Then calculate the middle value:

```python
mid = (left + right) // 2
```

We compare:

```python
mid * mid
```

with `num`.

### If `mid * mid == num`

We found an integer whose square is exactly `num`.

Therefore:

```python
return True
```

### If `mid * mid < num`

The square of `mid` is too small.

We need to search for a larger number:

```python
left = mid + 1
```

### If `mid * mid > num`

The square of `mid` is too large.

We need to search for a smaller number:

```python
right = mid - 1
```

If the Binary Search finishes without finding an exact square, then `num` is not a perfect square.

Therefore:

```python
return False
```

The key idea is:

> **Search for an integer whose square is exactly equal to `num` using Binary Search.**

---

## 🧠 Algorithm

1. Initialize:

   ```python
   left = 1
   right = num
   ```

2. While `left <= right`:
   - Calculate:

     ```python
     mid = (left + right) // 2
     ```

   - If `mid * mid == num`, return `True`.
   - If `mid * mid < num`, move `left` to `mid + 1`.
   - Otherwise, move `right` to `mid - 1`.

3. If the loop finishes without finding a perfect square, return `False`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log n)**

Binary Search eliminates approximately half of the possible values during every iteration.

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
- Search Space Reduction
- Mathematical Comparison
- Perfect Square
- Integer Arithmetic

---

## 🎯 Key Learning

- Binary Search can be used to solve mathematical problems by searching through a **range of possible answers**.
- Instead of calculating the square root directly, we search for an integer `mid` such that:

  ```python
  mid * mid == num
  ```

- If the square is too small, search right.
- If the square is too large, search left.
- This problem is very similar to **LeetCode 69 – Sqrt(x)**.
  - **69:** Find the integer square root.
  - **367:** Determine whether an exact integer square root exists.

- Both problems demonstrate **Binary Search on an answer space**.
- The solution runs in **O(log n) time and O(1) space**.
