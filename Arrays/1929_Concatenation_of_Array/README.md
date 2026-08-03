## 🔗 Problem

Given an integer array `nums` of length `n`, return an array `ans` of length `2n` such that:

- `ans[i] == nums[i]`
- `ans[i + n] == nums[i]`

for `0 <= i < n`.

In other words, return the concatenation of the array with itself.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,2,1]
```

**Output**

```text
[1,2,1,1,2,1]
```

---

### Example 2

**Input**

```text
nums = [1,3,2,1]
```

**Output**

```text
[1,3,2,1,1,3,2,1]
```

---

## 💡 Approach

### Array Traversal

- Determine the length of the input array.
- Create a new array of size `2 * n`.
- Traverse the original array once.
- Copy each element into:
  - its original position.
  - the corresponding position in the second half of the new array.
- Return the resulting array.

---

## 🧠 Algorithm

1. Find the length of the array `n`.
2. Create an array `ans` of size `2 * n`.
3. Traverse the array from `0` to `n - 1`.
4. Store:
   - `nums[i]` at `ans[i]`
   - `nums[i]` at `ans[i + n]`
5. Return `ans`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The array is traversed once.
- Each element is copied twice.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- A new array of size `2n` is created.

Ignoring constant factors,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Array
- Array Traversal
- Index Manipulation

---

## 🎯 Key Learning

- Learn how to create and initialize a new array.
- Practice copying elements using index manipulation.
- Understand the difference between modifying an existing array and creating a new one.
- This problem is a good introduction to array construction and indexing.
