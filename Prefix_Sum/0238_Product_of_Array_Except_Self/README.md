## 🔗 Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of all elements of nums except nums[i]
```

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

The solution must run in **O(n)** time and should not use division.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
[24,12,8,6]
```

Explanation:

```text
1 → 2 × 3 × 4 = 24
2 → 1 × 3 × 4 = 12
3 → 1 × 2 × 4 = 8
4 → 1 × 2 × 3 = 6
```

---

### Example 2

**Input**

```text
nums = [-1,1,0,-3,3]
```

**Output**

```text
[0,0,9,0,0]
```

---

# 💡 Approach 1 — Brute Force

For every index `i`, calculate the product of every element except `nums[i]`.

We use two loops:

- The outer loop chooses the element to exclude.
- The inner loop calculates the product of all other elements.

---

## ⏱ Brute Force Complexity

### Time Complexity: **O(n²)**

For every element, we traverse the entire array again.

### Space Complexity: **O(n)**

The output array requires `O(n)` space.

---

# 💡 Approach 2 — Prefix and Suffix Products

The optimized solution calculates the product of all elements **before** and **after** each index.

For every index:

```text
answer[i] =
product of elements to the left
×
product of elements to the right
```

We can calculate these two products using two passes.

---

## 🧠 Step 1 — Prefix Product

First, calculate the product of all elements to the **left** of each index.

For:

```text
nums = [1,2,3,4]
```

The prefix products stored in `result` become:

```text
[1,1,2,6]
```

For example:

```text
index 2 → elements on the left = [1,2]

1 × 2 = 2
```

---

## 🧠 Step 2 — Suffix Product

Then traverse from right to left and multiply each position by the product of all elements to its **right**.

For:

```text
nums = [1,2,3,4]
```

The suffix products are:

```text
[24,12,4,1]
```

Combining prefix and suffix products gives:

```text
[24,12,8,6]
```

---

## 🔍 Dry Run

For:

```text
nums = [1,2,3,4]
```

### Prefix pass

```text
result = [1,1,2,6]
```

Here `result[i]` contains everything **to the left** of `i`.

### Suffix pass

Starting from the right:

```text
result[3] = 6 × 1 = 6
result[2] = 2 × 4 = 8
result[1] = 1 × 12 = 12
result[0] = 1 × 24 = 24
```

Final result:

```text
[24,12,8,6]
```

---

## ⏱ Optimized Complexity

### Time Complexity: **O(n)**

We make two passes through the array.

```text
O(n) + O(n) = O(n)
```

### Space Complexity: **O(1)**

Apart from the output array, we only use a few variables:

```text
prefix
suffix
```

Therefore, the auxiliary space is:

```text
O(1)
```

---

## 📊 Comparison

| Approach        | Time Complexity | Extra Space |
| --------------- | --------------: | ----------: |
| Brute Force     |           O(n²) |        O(1) |
| Prefix + Suffix |        **O(n)** |    **O(1)** |

_The output array is not counted as extra space._

---

## 📚 Concepts Used

- Prefix Product
- Suffix Product
- Array Traversal
- In-place Result Construction

---

## 🎯 Key Learning

The key idea is:

```text
product except nums[i]
=
product of everything on the left
×
product of everything on the right
```

Instead of repeatedly calculating the product for every index, we calculate prefix and suffix products once.

This reduces the solution from:

```text
O(n²)
```

to:

```text
O(n)
```
