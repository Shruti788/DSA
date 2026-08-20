# 🔗 Problem

You are given an integer array `nums`.

You are initially positioned at the **first index** of the array.

Each element `nums[i]` represents the **maximum number of steps** you can jump forward from index `i`.

Return `True` if you can reach the **last index** of the array. Otherwise, return `False`.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,3,1,1,4]
```

**Output**

```text
true
```

**Explanation**

- Start at index `0`, where you can jump up to `2` steps.
- You can reach index `1`.
- From index `1`, you can jump up to `3` steps.
- This allows you to reach the last index.

Therefore, the answer is `True`.

---

## 💡 Approach

### Greedy + Farthest Reach

We keep track of the **farthest index we can reach** using a variable:

```python
farthest = 0
```

As we traverse the array:

- If the current index `i` is greater than `farthest`, it means we cannot even reach this position.
- Therefore, we immediately return `False`.
- Otherwise, we update the farthest position we can reach:

```python
farthest = max(farthest, i + nums[i])
```

The greedy idea is:

> **At every reachable index, keep the maximum possible reach.**

We don't need to decide exactly which jump to take. We only care about how far we can potentially reach.

---

## 🧠 Algorithm

1. Initialize `farthest = 0`.
2. Traverse the array from left to right.
3. For each index `i`:
   - Check if `i > farthest`.
   - If yes, return `False` because this index cannot be reached.
   - Otherwise, calculate how far we can reach from this index:

     ```python
     i + nums[i]
     ```

   - Update `farthest` with the maximum reachable position.

4. If the loop finishes, return `True`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- We traverse the array only once.
- Each index is processed exactly once.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We only use one extra variable:

```python
farthest
```

No additional data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Array Traversal
- Maximum Reach
- Range / Reachability

---

## 🎯 Key Learning

- In many **Greedy** problems, we don't need to find the exact sequence of choices.
- Instead, we can keep track of the **best possible state**.
- Here, `farthest` represents the maximum index we can currently reach.
- This greedy approach avoids trying every possible jump and solves the problem in **O(n) time and O(1) space**.
