## 🔗 Problem

Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

A subarray is a contiguous part of the array.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,1,1]
k = 2
```

**Output**

```text
2
```

The two subarrays are:

```text
[1,1]
[1,1]
```

---

### Example 2

**Input**

```text
nums = [1,2,3]
k = 3
```

**Output**

```text
2
```

The subarrays are:

```text
[1,2]
[3]
```

---

# 💡 Approach 1 — Brute Force

We consider every possible starting index and expand the subarray from that point.

For every `i`:

- Start `current_sum = 0`.
- Move `j` from `i` to the end.
- Add `nums[j]` to `current_sum`.
- Whenever `current_sum == k`, increment the count.

This avoids recalculating the sum of every subarray from scratch.

---

## ⏱ Brute Force Complexity

### Time Complexity: **O(n²)**

There are two nested loops.

The outer loop chooses the starting position, while the inner loop explores the remaining elements.

Therefore:

**Time Complexity = O(n²)**

### Space Complexity: **O(1)**

Only `count` and `current_sum` are used.

**Space Complexity = O(1)**

---

# 💡 Approach 2 — Prefix Sum + Hash Map

The optimized solution uses **Prefix Sum + Hash Map**.

Instead of checking every possible subarray, we keep track of prefix sums that we have already seen.

Suppose the current prefix sum is:

```text
current_sum
```

We want a previous prefix sum such that:

```text
current_sum - previous_sum = k
```

Rearranging:

```text
previous_sum = current_sum - k
```

So, while traversing the array, we check whether:

```python
current_sum - k
```

has already appeared.

If it has, those previous prefix sums represent subarrays whose sum is exactly `k`.

---

## 🧠 Optimized Algorithm

1. Create a dictionary to store the frequency of prefix sums.
2. Initialize:

```python
prefix_sum = 0
count = 0
```

3. Store:

```python
freq[0] = 1
```

This handles subarrays whose sum starts from index `0`.

4. Traverse through `nums`.
5. Add the current number to `prefix_sum`.
6. Check whether `prefix_sum - k` exists in the dictionary.
7. If it exists, add its frequency to `count`.
8. Store the current prefix sum in the dictionary.
9. Return `count`.

---

## ⏱ Optimized Complexity

### Time Complexity: **O(n)**

The array is traversed only once.

Dictionary lookup and insertion take **O(1)** on average.

Therefore:

**Time Complexity = O(n)**

### Space Complexity: **O(n)**

The hash map can store up to `n` different prefix sums.

Therefore:

**Space Complexity = O(n)**

---

## 📊 Comparison

| Approach              | Time Complexity | Space Complexity |
| --------------------- | --------------: | ---------------: |
| Brute Force           |           O(n²) |             O(1) |
| Prefix Sum + Hash Map |        **O(n)** |             O(n) |

---

## 📚 Concepts Used

- Array
- Prefix Sum
- Hash Map
- Subarrays
- Frequency Counting

---

## 🎯 Key Learning

The important transformation is:

```text
current_sum - previous_sum = k
```

Therefore:

```text
previous_sum = current_sum - k
```

A hash map allows us to quickly check whether that required previous prefix sum has appeared before.

This reduces the brute-force solution from **O(n²)** to **O(n)**.
