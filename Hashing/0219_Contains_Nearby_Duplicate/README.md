## 🔗 Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` such that:

```text
nums[i] == nums[j]
```

and

```text
abs(i - j) <= k
```

Otherwise, return `false`.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,2,3,1]
k = 3
```

**Output**

```text
true
```

The value `1` appears at indices `0` and `3`.

```text
|0 - 3| = 3
```

Since `3 <= k`, the answer is `true`.

---

### Example 2

**Input**

```text
nums = [1,0,1,1]
k = 1
```

**Output**

```text
true
```

The value `1` appears at indices `2` and `3`.

```text
|2 - 3| = 1
```

---

### Example 3

**Input**

```text
nums = [1,2,3,1,2,3]
k = 2
```

**Output**

```text
false
```

The duplicate values exist, but none of their occurrences are within distance `k`.

---

## 💡 Approach

### Hash Map

Use a dictionary called `seen` to store:

```text
number → most recent index
```

As we traverse the array:

1. Check if the current number already exists in `seen`.
2. If it does, calculate the distance between the current index and its previous index.
3. If the distance is less than or equal to `k`, return `True`.
4. Otherwise, update the number's index to the current index.
5. If no valid pair is found, return `False`.

---

## 🧠 Why Store the Latest Index?

Suppose we have:

```text
nums = [1,2,3,1,1]
```

When we encounter another `1`, we only care about its **closest previous occurrence**.

Therefore, after processing each number, we update:

```python
seen[nums[i]] = i
```

This ensures that `seen` contains the most recent index.

---

## 🔍 Example Walkthrough

For:

```text
nums = [1,2,3,1]
k = 3
```

Initially:

```text
seen = {}
```

### i = 0

```text
nums[0] = 1
```

Not in `seen`, so:

```text
seen = {1: 0}
```

### i = 1

```text
nums[1] = 2
```

```text
seen = {1: 0, 2: 1}
```

### i = 2

```text
nums[2] = 3
```

```text
seen = {1: 0, 2: 1, 3: 2}
```

### i = 3

```text
nums[3] = 1
```

`1` already exists at index `0`.

Calculate:

```text
3 - 0 = 3
```

Since:

```text
3 <= k
```

we return:

```text
True
```

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

We traverse the array once.

Dictionary lookup and insertion take **O(1)** on average.

Therefore:

**Time Complexity = O(n)**

---

### Space Complexity: **O(n)**

In the worst case, the dictionary stores every unique number.

Therefore:

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Hash Map
- Array Traversal
- Index Tracking
- Duplicate Detection

---

## 🎯 Key Learning

A hash map can store not only whether an element has appeared, but also **where it appeared**.

For this problem:

```text
number → latest index
```

This allows us to check the distance between duplicate values in **O(1)** average time.
