# 🔗 Problem

We are given a number `n` representing the range:

```text
[1, n]
```

A number is secretly picked from this range.

The goal is to find the **picked number**.

We are given a `guess()` API that tells us how our guess compares to the picked number:

```text
guess(num) returns:

-1 → your guess is higher than the picked number
 1 → your guess is lower than the picked number
 0 → your guess is correct
```

Return the picked number.

---

## 📝 Example 1

**Input**

```text
n = 10
pick = 6
```

**Output**

```text
6
```

**Explanation**

We use Binary Search to find the picked number `6`.

---

## 💡 Approach

### Binary Search

The possible answer lies between:

```python
left = 1
right = n
```

We calculate the middle number:

```python
mid = (left + right) // 2
```

Then we use the `guess()` API to determine which half of the search space contains the answer.

### If `guess(mid) == 0`

Our guess is correct.

```python
return mid
```

### If `guess(mid) == 1`

This means:

> Our guess is **lower than** the picked number.

Therefore, the picked number must be somewhere to the **right** of `mid`.

```python
left = mid + 1
```

### If `guess(mid) == -1`

This means:

> Our guess is **higher than** the picked number.

Therefore, the picked number must be somewhere to the **left** of `mid`.

```python
right = mid - 1
```

The key idea is:

> **Use the result of `guess(mid)` to eliminate half of the possible numbers after every guess.**

---

## 🧠 Algorithm

1. Initialize:

   ```python
   left = 1
   right = n
   ```

2. While `left <= right`:
   - Calculate:

     ```python
     mid = (left + right) // 2
     ```

   - Call `guess(mid)`.
   - If the result is `0`, return `mid`.
   - If the result is `1`, move `left` to `mid + 1`.
   - If the result is `-1`, move `right` to `mid - 1`.

3. Continue until the picked number is found.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log n)**

Each guess eliminates approximately half of the remaining possible numbers.

Therefore,

**Time Complexity = O(log n)**

---

### Space Complexity: **O(1)**

We only use:

- `left`
- `right`
- `mid`

No additional data structures are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Binary Search
- Search Space Reduction
- API / Function Calls
- Boundary Management

---

## 🎯 Key Learning

- Binary Search does not always require an actual array.
- Here, we perform Binary Search directly on the range.

### 💡 Small Code Improvement

Instead of calling `guess(mid)` multiple times:

```python
if guess(mid) == 0:
    return mid
elif guess(mid) == 1:
    left = mid + 1
else:
    right = mid - 1
```

you can store the result:

```python
result = guess(mid)

if result == 0:
    return mid
elif result == 1:
    left = mid + 1
else:
    right = mid - 1
```

This calls the API **only once per iteration**, which is cleaner and more efficient.
