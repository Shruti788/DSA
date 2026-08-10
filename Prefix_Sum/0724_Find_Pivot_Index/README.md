## 🔗 Problem

Given an integer array `nums`, find the **pivot index**.

The pivot index is the index where the sum of all elements to the left is equal to the sum of all elements to the right.

If no such index exists, return `-1`.

If there are multiple pivot indices, return the leftmost one.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,7,3,6,5,6]
```

**Output**

```text
3
```

**Explanation**

- Left sum = 1 + 7 + 3 = 11
- Right sum = 5 + 6 = 11

Since both sums are equal, the pivot index is `3`.

---

### Example 2

**Input**

```text
nums = [1,2,3]
```

**Output**

```text
-1
```

---

### Example 3

**Input**

```text
nums = [2,1,-1]
```

**Output**

```text
0
```

---

## 💡 Approach

### Prefix Sum

Instead of calculating the left and right sums separately for every index, maintain:

- `left_sum` → sum of elements to the left of the current index.
- `total_sum` → sum of the entire array.

For each index:

```text
right_sum = total_sum - left_sum - nums[i]
```

If `left_sum == right_sum`, then the current index is the pivot index.

After checking the current index, update:

```text
left_sum += nums[i]
```

This allows us to find the pivot index in a single traversal.

---

## 🧠 Algorithm

1. Calculate the total sum of the array.
2. Initialize `left_sum = 0`.
3. Traverse the array.
4. Compute:

```python
right_sum = total_sum - left_sum - nums[i]
```

5. If `left_sum == right_sum`, return the current index.
6. Otherwise, update:

```python
left_sum += nums[i]
```

7. If no pivot index is found, return `-1`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Calculating the total sum takes **O(n)**.
- Traversing the array once takes **O(n)**.

Overall,

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(1)**

- Only two extra variables (`left_sum` and `total_sum`) are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Array
- Prefix Sum
- Running Sum

---

## 🎯 Key Learning

- Prefix sums allow left and right sums to be calculated efficiently.
- Instead of recomputing sums for every index (**O(n²)**), maintain a running left sum and derive the right sum using the total sum.
- This reduces the solution to an optimal **O(n)** time complexity.
