# 🔗 Problem

You are given a sequence of versions:

```text
1, 2, 3, ..., n
```

At some point, a version becomes **bad**.

Once a version is bad, **all versions after it are also bad**.

You are given an API:

```python
isBadVersion(version)
```

which returns:

```text
True  → the version is bad
False → the version is good
```

Return the **first bad version**.

The solution must minimize the number of calls to the API.

---

## 📝 Example

### Example 1

**Input**

```text
n = 5
bad = 4
```

**Versions**

```text
1  2  3  4  5
G  G  G  B  B
```

**Output**

```text
4
```

**Explanation**

## Version `4` is the first bad version.

## 💡 Approach

### Binary Search

The versions have a special property:

```text
Good → Good → Good → Bad → Bad → Bad
```

This means we can use **Binary Search** to find the boundary between good and bad versions.

We initialize:

```python
left = 1
right = n
```

Then calculate the middle version:

```python
mid = (left + right) // 2
```

We check:

```python
isBadVersion(mid)
```

### If `mid` is bad

```python
if isBadVersion(mid):
    right = mid
```

Since `mid` is bad, the first bad version could be:

- `mid`
- Or somewhere before `mid`

So we keep `mid` in our search range.

This is why we use:

```python
right = mid
```

instead of:

```python
right = mid - 1
```

---

### If `mid` is good

If `mid` is good, then the first bad version must be **after `mid`**.

Therefore:

```python
left = mid + 1
```

---

## 🧠 Algorithm

1. Initialize:

   ```python
   left = 1
   right = n
   ```

2. While `left < right`:
   - Calculate:

     ```python
     mid = (left + right) // 2
     ```

   - If `mid` is bad:

     ```python
     right = mid
     ```

   - Otherwise:

     ```python
     left = mid + 1
     ```

3. When `left == right`, the search has narrowed down to exactly one version.
4. Return `left`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(log n)**

Every API call eliminates approximately half of the remaining versions.

Therefore:

**Time Complexity = O(log n)**

---

### Space Complexity: **O(1)**

We only use:

- `left`
- `right`
- `mid`

No additional data structures are required.

Therefore:

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Binary Search
- Boundary Search
- Search Space Reduction
- API Calls
- First Occurrence / First True Position

---

## 🎯 Key Learning

- Binary Search can be used to find a **boundary**, not just an exact value.
- The versions have a monotonic pattern:

  ```text
  Good → Bad
  ```

- When `mid` is bad, keep `mid` because it could be the first bad version:

  ```python
  right = mid
  ```

- When `mid` is good, eliminate it and everything before it:

  ```python
  left = mid + 1
  ```

- When `left == right`, we have found the **first bad version**.
- This is a fundamental **Binary Search on a monotonic condition** pattern.
