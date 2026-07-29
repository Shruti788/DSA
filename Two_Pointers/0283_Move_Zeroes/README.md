## 🔗 Problem

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

You must modify the array **in-place** without making a copy of the array.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [0,1,0,3,12]
```

**Output**

```text
[1,3,12,0,0]
```

---

### Example 2

**Input**

```text
nums = [0]
```

**Output**

```text
[0]
```

---

## 💡 Approach

### Two Pointers

Use two pointers to keep track of where the next non-zero element should be placed.

- Initialize `left` to `0`.
- Traverse the array using `right`.
- Whenever a non-zero element is found, swap it with the element at the `left` pointer.
- Increment `left` after every successful swap.
- By the end of the traversal, all non-zero elements are moved to the front while all zeroes automatically shift to the end.

---

## 🧠 Algorithm

1. Initialize `left = 0`.
2. Traverse the array using `right`.
3. If `nums[right]` is not `0`:
   - Swap `nums[left]` and `nums[right]`.
   - Increment `left`.
4. Continue until the end of the array.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The array is traversed only once.
- Each element is processed exactly once.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(1)**

- The array is modified in-place.
- No extra data structures are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- In-Place Array Modification
- Swapping
- Array Traversal

---

## 🎯 Key Learning

- The **Two Pointers** technique allows us to rearrange elements efficiently without using extra space.
- Swapping non-zero elements into their correct positions preserves their relative order.
- Since the array is modified in-place, the solution achieves **O(1)** extra space.
