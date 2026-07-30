## 🔗 Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number, also sorted in non-decreasing order.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [-4,-1,0,3,10]
```

**Output**

```text
[0,1,9,16,100]
```

---

### Example 2

**Input**

```text
nums = [-7,-3,2,3,11]
```

**Output**

```text
[4,9,9,49,121]
```

---

## 💡 Approach

### Two Pointers

Although the array is sorted, squaring negative numbers changes their order.

- Initialize one pointer (`left`) at the beginning and another (`right`) at the end of the array.
- Compare the absolute values of both elements.
- The element with the larger absolute value produces the larger square.
- Place that square at the end of the result array.
- Move the corresponding pointer inward.
- Repeat until all elements have been processed.

This ensures the result array remains sorted.

---

## 🧠 Algorithm

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. Create a result array of the same size.
3. Initialize `index = len(nums) - 1`.
4. While `left <= right`:
   - Compare `abs(nums[left])` and `abs(nums[right])`.
   - Place the larger square at `result[index]`.
   - Move the corresponding pointer.
   - Decrement `index`.
5. Return the result array.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The `left` and `right` pointers each move toward the center.
- Every element is processed exactly once.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- A new result array of size `n` is created to store the sorted squares.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Two Pointers
- Array Traversal
- Absolute Value
- Sorted Array

---

## 🎯 Key Learning

- A sorted array containing negative numbers cannot simply be squared and remain sorted.
- Comparing the absolute values at both ends allows us to determine the next largest square.
- Filling the result array from the end guarantees the final array remains sorted.
- This approach improves the brute-force sorting solution from **O(n log n)** to **O(n)**.
