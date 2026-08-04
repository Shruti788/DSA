## 🔗 Problem

Given an array `nums`, return the running sum of `nums`.

The running sum of an array is defined as:

```text
runningSum[i] = sum(nums[0]...nums[i])
```

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
[1,3,6,10]
```

**Explanation**

```text
runningSum[0] = 1
runningSum[1] = 1 + 2 = 3
runningSum[2] = 1 + 2 + 3 = 6
runningSum[3] = 1 + 2 + 3 + 4 = 10
```

---

### Example 2

**Input**

```text
nums = [1,1,1,1,1]
```

**Output**

```text
[1,2,3,4,5]
```

---

## 💡 Approach

### Prefix Sum (Running Sum)

Create a new array to store the running sum.

- Initialize the first element of the answer array with the first element of `nums`.
- Traverse the remaining elements.
- Each running sum is obtained by adding the current element to the previous running sum.
- Return the completed array.

---

## 🧠 Algorithm

1. Find the length of the array.
2. Create an answer array of the same size.
3. Set:

```python
ans[0] = nums[0]
```

4. Traverse from index `1` to `n - 1`.
5. Compute:

```python
ans[i] = ans[i - 1] + nums[i]
```

6. Return `ans`.

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

- A new array of size `n` is created to store the running sums.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Array
- Prefix Sum
- Array Traversal

---

## 🎯 Key Learning

- Prefix sums allow cumulative values to be computed efficiently.
- Each running sum depends on the previous running sum instead of recomputing the entire prefix.
- Prefix sums are a fundamental technique used in many array and range-sum problems.
