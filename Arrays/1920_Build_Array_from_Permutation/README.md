## 🔗 Problem

Given a zero-based permutation `nums` (0-indexed), build an array `ans` of the same length where:

- `ans[i] = nums[nums[i]]`

Return the constructed array.

A permutation is an array containing each integer from `0` to `n - 1` exactly once.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [0,2,1,5,3,4]
```

**Output**

```text
[0,1,2,4,5,3]
```

**Explanation**

```text
ans[0] = nums[nums[0]] = nums[0] = 0
ans[1] = nums[nums[1]] = nums[2] = 1
ans[2] = nums[nums[2]] = nums[1] = 2
ans[3] = nums[nums[3]] = nums[5] = 4
ans[4] = nums[nums[4]] = nums[3] = 5
ans[5] = nums[nums[5]] = nums[4] = 3
```

---

### Example 2

**Input**

```text
nums = [5,0,1,2,3,4]
```

**Output**

```text
[4,5,0,1,2,3]
```

---

## 💡 Approach

### Array Traversal

- Find the length of the array.
- Create a new array `ans` of the same size.
- Traverse the input array.
- For every index `i`, store `nums[nums[i]]` in `ans[i]`.
- Return the newly constructed array.

---

## 🧠 Algorithm

1. Find the length of the array `n`.
2. Create an array `ans` of size `n`.
3. Traverse the array from `0` to `n - 1`.
4. Assign:

```python
ans[i] = nums[nums[i]]
```

5. Return `ans`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The array is traversed once.
- Each element is processed exactly once.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- A new array of size `n` is created.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Array
- Array Traversal
- Index Manipulation
- Permutation

---

## 🎯 Key Learning

- Learn how to access elements using values as indices.
- Practice constructing a new array from an existing array.
- Understand how permutations can be used for indirect indexing.
- This problem strengthens understanding of array indexing and traversal.
