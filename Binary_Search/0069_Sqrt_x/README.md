# 🔗 Problem

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer.

The returned integer must be the **largest integer whose square is less than or equal to `x`**.

You must not use any built-in exponentiation functions or operators.

---

## 📝 Example

### Example 1

**Input**

```text
x = 4
```

**Output**

```text
2
```

**Explanation**

```text
2 × 2 = 4
```

Therefore, the square root of `4` is `2`.

---

## 💡 Approach

### Binary Search

Instead of calculating the square root directly, we search for the answer using **Binary Search**.

For a number `x`, the integer square root must lie between:

```python
left = 1
right = x
```

We calculate the middle value:

```python
mid = (left + right) // 2
```

Then compare:

```python
mid * mid
```

with `x`.

### If `mid * mid == x`

We found the exact square root:

```python
return mid
```

### If `mid * mid < x`

The value of `mid` is too small.

The square root may be `mid` or a larger value, so we search the right half:

```python
left = mid + 1
```

### If `mid * mid > x`

The value of `mid` is too large.

So we search the left half:

```python
right = mid - 1
```

If `x` is not a perfect square, the loop eventually ends with:

```text
left > right
```

At that point, `right` represents the largest integer whose square is less than `x`.

Therefore:

```python
return right
```

---

## 🧠 Algorithm

1. If `x < 2`, return `x`.
2. Initialize:

   ```python
   left = 1
   right = x
   ```

3. While `left <= right`:
   - Calculate:

     ```python
     mid = (left + right) // 2
     ```

   - If `mid * mid == x`, return `mid`.
   - If `mid * mid < x`, move `left` to `mid + 1`.
   - Otherwise, move `right` to `mid - 1`.

4. If no exact square root is found, return `right`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log x)**

Binary Search eliminates approximately half of the search range during every iteration.

Therefore:

**Time Complexity = O(log x)**

---

### Space Complexity: **O(1)**

We only use a few variables:

- `left`
- `right`
- `mid`

No additional data structures are used.

Therefore:

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Binary Search
- Search Space
- Integer Square Root
- Boundary Search
- Mathematical Comparison

---

## 🎯 Key Learning

- Binary Search can be performed on a **range of possible answers**, not just on an array.
- `mid * mid` helps us determine whether our current guess is too small or too large.
- If the exact square root does not exist, Binary Search still helps us find the correct rounded-down answer.
- After the loop ends:

  ```text
  left = first value whose square is greater than x
  right = largest value whose square is less than x
  ```

- Therefore, returning `right` gives the integer square root.
- This problem is an important example of **Binary Search on Answer Space**.
