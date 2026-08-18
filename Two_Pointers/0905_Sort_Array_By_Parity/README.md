## 🔗 Problem

Given an integer array `nums`, move all the **even integers** to the beginning of the array followed by all the **odd integers**.

Return any array that satisfies this condition.

The relative order of the even and odd numbers does not matter.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [3,1,2,4]
```

**Output**

```text
[2,4,3,1]
```

The even numbers:

```text
2,4
```

are placed before the odd numbers:

```text
3,1
```

---

### Example 2

**Input**

```text
nums = [0,1]
```

**Output**

```text
[0,1]
```

`0` is even, so it is already at the beginning.

---

## 💡 Approach

### Two Pointers

Use two pointers:

```text
left  → starts from the beginning
right → starts from the end
```

The goal is:

```text
left  → find an odd number
right → find an even number
```

Once we find:

```text
nums[left] = odd
nums[right] = even
```

we swap them.

We continue until:

```text
left >= right
```

---

## 🧠 How the Two Pointers Work

We start with:

```python
left = 0
right = len(nums) - 1
```

Then:

```python
while left < right:
```

This means we continue working while the two pointers have not crossed each other.

### Left Pointer

The left pointer should stop when it finds an **odd number**.

Therefore:

```python
while left < right and nums[left] % 2 == 0:
    left += 1
```

If `nums[left]` is even, it is already in the correct section, so we move `left` forward.

Eventually:

```text
nums[left] = odd
```

---

### Right Pointer

The right pointer should stop when it finds an **even number**.

Therefore:

```python
while left < right and nums[right] % 2 == 1:
    right -= 1
```

If `nums[right]` is odd, it is already in the correct section, so we move `right` backward.

Eventually:

```text
nums[right] = even
```

---

### Swap

Now we have:

```text
left  → odd
right → even
```

So we swap them:

```python
nums[left], nums[right] = nums[right], nums[left]
```

This puts:

```text
even → left side
odd  → right side
```

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

Both pointers move only in one direction.

`left` moves from the beginning toward the end, while `right` moves from the end toward the beginning.

Together, they process the array at most a constant number of times.

Therefore:

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We modify the array **in-place** and only use two variables:

```python
left
right
```

No additional array or data structure is required.

Therefore:

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- Array Traversal
- In-Place Modification
- Partitioning
- Even and Odd Numbers

---

## 🎯 Key Learning

The key idea is to use **two pointers moving toward each other**.

This pattern is useful for many **array partitioning and two-pointer problems**.
