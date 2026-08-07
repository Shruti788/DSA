## 🔗 Problem

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [-1,0,1,2,-1,-4]
```

**Output**

```text
[[-1,-1,2],[-1,0,1]]
```

---

### Example 2

**Input**

```text
nums = [0,1,1]
```

**Output**

```text
[]
```

---

### Example 3

**Input**

```text
nums = [0,0,0]
```

**Output**

```text
[[0,0,0]]
```

---

## 💡 Approach

### Sorting + Two Pointers

1. Sort the array.
2. Fix one element using a loop.
3. Use two pointers (`left` and `right`) to search for the remaining two numbers.
4. Calculate the sum:
   - If the sum is less than `0`, move `left` forward.
   - If the sum is greater than `0`, move `right` backward.
   - If the sum is `0`, store the triplet.
5. Skip duplicate values to avoid repeated triplets.

This approach efficiently finds all unique triplets.

---

## 🧠 Algorithm

1. Sort the array.
2. Iterate through the array using index `i`.
3. Skip duplicate values for `i`.
4. Initialize:
   - `left = i + 1`
   - `right = len(nums) - 1`
5. While `left < right`:
   - Calculate the total sum.
   - Move pointers according to the sum.
   - If the sum is `0`:
     - Store the triplet.
     - Move both pointers.
     - Skip duplicate values for `left` and `right`.
6. Return the list of unique triplets.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n²)**

- Sorting the array takes **O(n log n)**.
- The outer loop runs **n** times.
- The two pointers together traverse the remaining array once for each fixed element.

Overall,

**Time Complexity = O(n²)**

---

### Space Complexity: **O(1)** _(excluding the output list)_

- The algorithm uses only a few extra variables.
- The output list is not counted in the auxiliary space complexity.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Sorting
- Two Pointers
- Array Traversal
- Duplicate Handling

---

## 🎯 Key Learning

- Sorting enables the efficient use of two pointers.
- Skipping duplicate values ensures that each triplet is unique.
- Using two pointers after fixing one element reduces the brute-force solution from **O(n³)** to **O(n²)**.
- This problem is a classic example of combining multiple techniques to achieve an optimal solution.
