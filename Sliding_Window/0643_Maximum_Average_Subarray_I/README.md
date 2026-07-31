## 🔗 Problem

You are given an integer array `nums` consisting of `n` elements and an integer `k`.

Find a contiguous subarray of length `k` that has the maximum average value and return this value.

Any answer with a calculation error of less than `10^-5` will be accepted.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

**Output**

```text
12.75
```

**Explanation**

The subarray with the maximum average is:

```text
[12, -5, -6, 50]
```

Sum = 51

Average = 51 / 4 = 12.75

---

### Example 2

**Input**

```text
nums = [5]
k = 1
```

**Output**

```text
5.0
```

---

## 💡 Approach

### Sliding Window

Instead of calculating the sum of every subarray from scratch, maintain a window of size `k`.

- Calculate the sum of the first `k` elements.
- Store it as the current maximum sum.
- Slide the window one element at a time:
  - Remove the element leaving the window.
  - Add the new element entering the window.
- Update the maximum sum whenever a larger window sum is found.
- Return the maximum average by dividing the maximum sum by `k`.

This avoids recalculating the sum for every window and makes the solution efficient.

---

## 🧠 Algorithm

1. Calculate the sum of the first `k` elements.
2. Store it in `window_sum` and `max_sum`.
3. Traverse the remaining elements:
   - Remove the element leaving the window.
   - Add the new element entering the window.
   - Update `max_sum` if needed.
4. Return `max_sum / k`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Calculating the initial window sum takes **O(k)**.
- Sliding the window across the remaining elements takes **O(n - k)**.
- Therefore, the total time complexity is:

**O(k + (n - k)) = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(1)**

- Only a few variables are used (`window_sum`, `max_sum`, and `i`).
- No extra data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Sliding Window
- Array Traversal
- Running Sum

---

## 🎯 Key Learning

- The **Sliding Window** technique efficiently processes fixed-size subarrays by updating the window sum instead of recomputing it.
- Removing the outgoing element and adding the incoming element reduces the time complexity from **O(n × k)** (brute force) to **O(n)**.
- This pattern is commonly used in interview problems involving contiguous subarrays or substrings.
