# 🔗 Problem

You are given an array `boxTypes`, where:

```text
boxTypes[i] = [numberOfBoxes, numberOfUnitsPerBox]
```

You are also given an integer `truckSize`, representing the maximum number of boxes that the truck can carry.

Each box type contains a certain number of boxes, and every box of that type contains the same number of units.

Return the **maximum total number of units** that can be loaded onto the truck.

---

## 📝 Example

### Example 1

**Input**

```text
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
```

**Output**

```text
8
```

**Explanation**

Sort the box types by units per box:

```text
[[1,3],[2,2],[3,1]]
```

Take:

- 1 box × 3 units = 3 units
- 2 boxes × 2 units = 4 units
- 1 box × 1 unit = 1 unit

Total:

```text
3 + 4 + 1 = 8
```

---

## 💡 Approach

### Greedy + Sorting

The goal is to maximize the number of units in the truck.

Therefore, we should always choose the box type that gives us the **most units per box first**.

First, sort `boxTypes` in descending order based on `unitsPerBox`:

```python
boxTypes.sort(key=lambda x: x[1], reverse=True)
```

For every box type, we calculate how many boxes we can actually take:

```python
boxes = min(boxType[0], truckSize)
```

We use `min()` because we cannot take more boxes than:

- The number of boxes available.
- The remaining capacity of the truck.

Then we calculate the units:

```python
total_units += boxes * boxType[1]
```

After loading the boxes, we reduce the remaining truck capacity:

```python
truckSize -= boxes
```

If the truck becomes full, we stop:

```python
if truckSize == 0:
    break
```

The greedy idea is:

> **Always take boxes with the highest units per box first.**

This gives the maximum possible number of units because every available truck space is prioritized for the most valuable boxes.

---

## 🧠 Algorithm

1. Sort `boxTypes` by `unitsPerBox` in descending order.
2. Initialize:

   ```python
   total_units = 0
   ```

3. Traverse each `boxType`.
4. Calculate how many boxes can fit:

   ```python
   boxes = min(boxType[0], truckSize)
   ```

5. Add their units to `total_units`.
6. Reduce `truckSize` by the number of boxes taken.
7. If `truckSize == 0`, stop the loop.
8. Return `total_units`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n)**

Let `n` be the number of box types.

- Sorting `boxTypes` takes **O(n log n)**.
- Traversing the box types takes **O(n)**.

Therefore,

**Time Complexity = O(n log n)**

---

### Space Complexity: **O(1)**

Apart from the sorting operation, we only use a few variables:

- `total_units`
- `boxes`
- `truckSize`

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Array Traversal
- Maximum Optimization

---

## 🎯 Key Learning

- When the goal is to **maximize something with limited capacity**, a Greedy approach can often work.
- Sort items based on their **value per unit of capacity**.
- Here, the value is `unitsPerBox`, so we prioritize the box type with the highest units per box.
- `min()` helps us handle cases where the truck cannot take all available boxes.
- We stop as soon as the truck becomes full.
- This problem is a classic example of **Greedy + Sorting** with **O(n log n) time**.
