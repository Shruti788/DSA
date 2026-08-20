# 🔗 Problem

You are given two arrays:

- `g` represents the **greed factor** of each child.
- `s` represents the **size** of each cookie.

A child is satisfied if the cookie size is **greater than or equal to** the child's greed factor.

Each child can receive at most one cookie, and each cookie can be given to at most one child.

Return the **maximum number of children** that can be satisfied.

---

## 📝 Example

### Example 1

**Input**

```text
g = [1,2,3]
s = [1,1]
```

**Output**

```text
1
```

Only the child with greed factor `1` can be satisfied.

---

## 💡 Approach

### Greedy + Sorting + Two Pointers

First, sort both arrays:

```python
g.sort()
s.sort()
```

Then use two pointers:

- `i` points to the current child.
- `j` points to the current cookie.

For each cookie:

- If the cookie can satisfy the current child (`s[j] >= g[i]`):
  - Give the cookie to the child.
  - Move both pointers forward.

- Otherwise:
  - The cookie is too small for the current child.
  - Move only the cookie pointer forward and try the next cookie.

The greedy idea is:

> **Use the smallest cookie that can satisfy the least greedy child.**

This avoids wasting a larger cookie on a child who could have been satisfied with a smaller one.

---

## 🧠 Algorithm

1. Sort the greed array `g`.
2. Sort the cookie array `s`.
3. Initialize `i = 0` for children.
4. Initialize `j = 0` for cookies.
5. While both pointers are within their arrays:
   - If `s[j] >= g[i]`:
     - The child can be satisfied.
     - Increment `i`.
     - Increment `j`.

   - Otherwise:
     - The cookie is too small.
     - Increment only `j`.

6. Return `i`, which represents the number of satisfied children.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n + m log m)**

Let:

- `n` = number of children

- `m` = number of cookies

- Sorting `g` takes **O(n log n)**.

- Sorting `s` takes **O(m log m)**.

- The two-pointer traversal takes **O(n + m)**.

Therefore,

**Time Complexity = O(n log n + m log m)**

---

### Space Complexity: **O(1)**

Apart from the sorting operation, we only use two pointer variables:

- `i`
- `j`

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Two Pointers
- Array Traversal

---

## 🎯 Key Learning

- Sorting helps us make the greedy choice efficiently.
- Always try to satisfy the **least greedy child first**.
- Use the **smallest cookie that can satisfy** the current child.
- If a cookie is too small, don't waste it on a more greedy child — simply move to the next cookie.
- This problem is a great example of combining **Greedy + Sorting + Two Pointers**.
