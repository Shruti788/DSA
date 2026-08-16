## 🔗 Problem

Given an array `nums` containing `0`, `1`, and `2`, sort the array **in-place** so that objects of the same color are adjacent, with the colors in the order:

```text
0 → 1 → 2
```

You must solve the problem **without using the library's sort function**.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,0,2,1,1,0]
```

**Output**

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input**

```text
nums = [2,0,1]
```

**Output**

```text
[0,1,2]
```

---

## 💡 Approach

This problem can be solved using the **Dutch National Flag Algorithm**.

We use **three pointers**:

```text
low
mid
high
```

### What each pointer means

```text
low
 ↓
[ 0s | unknown | 1s | unknown | 2s ]
      ↑                 ↑
     mid               high
```

- `low` → position where the next `0` should go.
- `mid` → current element we are checking.
- `high` → position where the next `2` should go.

Our goal is to divide the array into four regions:

```text
[ 0s | 1s | unknown | 2s ]
```

As we process elements, the `unknown` region becomes smaller.

---

## 🔍 Three Cases

At every step, we check:

```python
nums[mid]
```

There are only three possibilities.

### Case 1: `nums[mid] == 0`

A `0` belongs on the left.

So we swap `nums[mid]` with `nums[low]`.

```python
nums[low], nums[mid] = nums[mid], nums[low]
```

Then move both pointers:

```python
low += 1
mid += 1
```

Why both?

Because the `0` has been placed correctly, and the element moved to `mid` from `low` has already been processed.

---

### Case 2: `nums[mid] == 1`

A `1` already belongs in the middle.

So we don't need to swap anything.

Simply move:

```python
mid += 1
```

---

### Case 3: `nums[mid] == 2`

A `2` belongs on the right.

So swap:

```python
nums[mid], nums[high] = nums[high], nums[mid]
```

Then move:

```python
high -= 1
```

### ⚠️ Important

We **do not increase `mid`** here.

Why?

Because the element that came from `high` has **not been checked yet**.

For example:

```text
[0, 1, 2, 0, 1]
       ↑     ↑
      mid   high
```

If `nums[mid] == 2`, we swap:

```text
[0, 1, 1, 0, 2]
       ↑     ↑
      mid   high
```

The new element at `mid` is `1`.

We still need to check it.

That's why we only do:

```python
high -= 1
```

## and leave `mid` where it is.

## ⏱️ Complexity

### Time Complexity

```text
O(n)
```

The `mid` and `high` pointers move across the array, so every element is processed a constant number of times.

### Space Complexity

```text
O(1)
```

We only use three pointers and perform the sorting **in-place**.

---

## 🧠 Key Pattern

This problem uses the:

**Dutch National Flag Algorithm**

The basic idea is:

```text
0 → LEFT
1 → MIDDLE
2 → RIGHT
```

---

## 🎯 What I Learned

- How to use **three pointers** to partition an array.
- How to sort an array in-place without using `.sort()`.
- How the **Dutch National Flag Algorithm** works.
- Why `mid` moves differently depending on the value.
- Why `mid` should **not** be incremented when we encounter `2`.
- How multiple pointers can divide an array into different regions.

---
