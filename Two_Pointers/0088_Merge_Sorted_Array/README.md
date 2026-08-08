## 🔗 Problem

You are given two sorted integer arrays `nums1` and `nums2`.

- `nums1` has enough space at the end to hold all elements of `nums2`.
- `m` represents the number of valid elements in `nums1`.
- `n` represents the number of elements in `nums2`.

Merge `nums2` into `nums1` so that `nums1` becomes one sorted array.

The merge must be performed **in-place**.

---

## 📝 Example

### Example 1

**Input**

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

**Output**

```text
[1,2,2,3,5,6]
```

---

### Example 2

**Input**

```text
nums1 = [1]
m = 1

nums2 = []
n = 0
```

**Output**

```text
[1]
```

---

## 💡 Approach 1 — Brute Force

A simple approach is to place all elements of `nums2` into the empty positions of `nums1`.

Then sort the entire `nums1` array.

### Complexity

**Time Complexity: O((m+n) log(m+n))**

The entire merged array is sorted.

**Space Complexity: O(1)**

The merge is performed inside `nums1`.

Although this approach works, it does not take advantage of the fact that both arrays are already sorted.

---

# 💡 Approach 2 — Optimized Two Pointers

Because both arrays are already sorted, we can merge them without sorting again.

The important idea is to start **from the end**.

We use three pointers:

```text
i → last valid element in nums1
j → last element in nums2
k → last available position in nums1
```

For example:

```text
nums1 = [1,2,3,0,0,0]
          ↑       ↑
          i       k

nums2 = [2,5,6]
          ↑
          j
```

Compare `nums1[i]` and `nums2[j]`.

- Put the larger value at `nums1[k]`.
- Move the corresponding pointer backward.
- Move `k` backward.

We work from right to left so that we don't overwrite the unprocessed elements in `nums1`.

---

## 🧠 Algorithm

1. Set `i = m - 1`.
2. Set `j = n - 1`.
3. Set `k = m + n - 1`.
4. While `j >= 0`:
   - Compare `nums1[i]` and `nums2[j]`.
   - Put the larger element at `nums1[k]`.
   - Move the corresponding pointer backward.
   - Decrease `k`.
5. Stop when all elements from `nums2` have been placed.

---

## ⏱ Complexity Analysis

### Brute Force

**Time Complexity: O((m+n) log(m+n))**

Because the resulting array is sorted after inserting `nums2`.

**Space Complexity: O(1)**

---

### Optimized Two Pointers

**Time Complexity: O(m+n)**

Each element is processed at most once.

**Space Complexity: O(1)**

The merge happens directly inside `nums1`.

---

## 📊 Comparison

| Approach           |              Time |    Space |
| ------------------ | ----------------: | -------: |
| Brute Force + Sort | O((m+n) log(m+n)) |     O(1) |
| Two Pointers       |        **O(m+n)** | **O(1)** |

---

## 🎯 Key Learning

The most important idea in this problem is **merging from the back**.

If we started from the beginning, placing an element into `nums1` could overwrite an element that we still need to process.

By starting from the end:

```text
i = m - 1
j = n - 1
k = m + n - 1
```

we can safely modify `nums1` in-place.

This is a very important **Two Pointers + In-place Array** pattern.

---

## 📚 Concepts Used

- Two Pointers
- In-place Array Modification
- Merging Sorted Arrays
- Sorting
