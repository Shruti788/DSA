## 🔗 Problem

Given a **1-indexed** array of integers `numbers` that is sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target`.

Return the indices of the two numbers (1-indexed) as an integer array of length 2.

---

## 📝 Example

### Example 1

**Input**

```text
numbers = [2,7,11,15]
target = 9
```

**Output**

```text
[1,2]
```

---

### Example 2

**Input**

```text
numbers = [2,3,4]
target = 6
```

**Output**

```text
[1,3]
```

---

## 💡 Approach

### Two Pointers

Since the array is already sorted, we can use two pointers.

- Place one pointer (`left`) at the beginning.
- Place another pointer (`right`) at the end.
- Calculate the sum of the two elements.
- If the sum equals the target, return their 1-based indices.
- If the sum is smaller than the target, move the left pointer one step to the right.
- If the sum is greater than the target, move the right pointer one step to the left.

This eliminates unnecessary comparisons and solves the problem efficiently.

---

## 🧠 Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(numbers) - 1`.
3. While `left < right`:
   - Calculate the current sum.
   - If the sum equals the target, return the 1-based indices.
   - If the sum is less than the target, increment `left`.
   - Otherwise, decrement `right`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The `left` and `right` pointers move toward each other.
- Each pointer moves at most `n` times.
- Every element is processed at most once.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

- No extra data structures are used.
- Only two pointer variables are maintained.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- Sorted Array
- Array Traversal

---

## 🎯 Key Learning

- When an array is sorted, the **Two Pointers** technique often provides a more efficient solution than using a Hash Map.
- By moving the pointers based on the current sum, we avoid checking every possible pair, reducing the time complexity from **O(n²)** to **O(n)** while using only **O(1)** extra space.
