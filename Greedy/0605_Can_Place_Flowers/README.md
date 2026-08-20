# 🔗 Problem

You are given a flowerbed represented by an array `flowerbed`, where:

- `0` represents an empty plot.
- `1` represents a plot where a flower is already planted.

Flowers cannot be planted in **adjacent plots**.

Given an integer `n`, return `True` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule. Otherwise, return `False`.

---

## 📝 Example

### Example 1

**Input**

```text
flowerbed = [1,0,0,0,1]
n = 1
```

**Output**

```text
true
```

A flower can be planted in the middle:

```text
[1,0,1,0,1]
```

---

## 💡 Approach

### Greedy + Array Traversal

We traverse the flowerbed from left to right.

For every position, we check three things:

- The current position is empty.
- The left position is empty or doesn't exist.
- The right position is empty or doesn't exist.

We use:

```python
left = (i == 0 or flowerbed[i-1] == 0)
right = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
```

If all conditions are satisfied, we immediately plant a flower:

```python
flowerbed[i] = 1
n -= 1
```

The greedy idea is:

> **Whenever we find a valid position, plant a flower immediately.**

We don't need to try different arrangements because planting at the earliest valid position leaves enough space for the remaining positions.

If `n` becomes `0`, we immediately return `True`.

---

## 🧠 Algorithm

1. If `n == 0`, return `True`.
2. Traverse every position in `flowerbed`.
3. For each position:
   - Check whether the current position is empty.
   - Check whether the left side is empty or the position is at the beginning.
   - Check whether the right side is empty or the position is at the end.

4. If all conditions are satisfied:
   - Plant a flower by setting `flowerbed[i] = 1`.
   - Decrease `n` by `1`.

5. If `n` becomes `0`, return `True`.
6. After traversing the entire flowerbed, return `n == 0`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

Let `n` represent the length of the `flowerbed` array.

- We traverse the flowerbed once.
- Each position is checked only once.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We only use a few variables:

- `i`
- `left`
- `right`
- `n`

No additional data structures are created.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Array Traversal
- Boundary Conditions
- In-place Modification

---

## 🎯 Key Learning

- A **Greedy** approach can solve the problem by making the best valid choice at every position.
- Whenever a flower can be safely planted, we should **plant it immediately**.
- Boundary positions require special handling because they don't have both a left and right neighbor.
- The conditions `i == 0` and `i == len(flowerbed) - 1` allow us to handle the edges without accessing invalid indices.
- Modifying the array in-place helps us remember newly planted flowers while continuing the traversal.
- This problem is a good example of **Greedy + Array Traversal** with **O(n) time and O(1) space**.
