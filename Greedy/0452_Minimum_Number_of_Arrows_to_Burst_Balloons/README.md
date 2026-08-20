# 🔗 Problem

There are several spherical balloons on a wall represented by intervals `[x_start, x_end]`.

An arrow can be shot vertically upward from any point on the x-axis and will burst all balloons whose intervals contain that point.

Find the **minimum number of arrows** required to burst all the balloons.

---

## 📝 Example

### Example 1

**Input**

```text
points = [[10,16],[2,8],[1,6],[7,12]]
```

**Output**

```text
2
```

**Explanation**

- Shoot one arrow at `x = 6` → bursts `[2,8]` and `[1,6]`.
- Shoot another arrow at `x = 11` → bursts `[10,16]` and `[7,12]`.

Therefore, the minimum number of arrows is `2`.

---

## 💡 Approach

### Greedy + Sorting

We sort the balloons based on their **ending points**.

```python
points.sort(key=lambda x: x[1])
```

Then we place the first arrow at the ending point of the first balloon.

For every following balloon:

- If its starting point is **less than or equal to** the current arrow position, the same arrow can burst it.
- Otherwise, the current arrow cannot burst it, so we need a new arrow.
- We place the new arrow at the ending point of that balloon.

The greedy idea is:

> **Always place the arrow at the earliest possible ending point.**

This gives the arrow the best chance of bursting as many upcoming balloons as possible.

---

## 🧠 Algorithm

1. Sort `points` by their ending point.
2. Initialize `arrows = 1`.
3. Set `end_point` to the ending point of the first balloon.
4. Traverse the remaining balloons:
   - If `points[i][0] <= end_point`, the current arrow can burst this balloon.
   - Otherwise:
     - Increment `arrows`.
     - Update `end_point` to the ending point of the current balloon.

5. Return `arrows`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n)**

- Sorting the intervals takes **O(n log n)**.
- Traversing the intervals takes **O(n)**.

Therefore,

**Time Complexity = O(n log n)**

---

### Space Complexity: **O(1)**

Apart from the sorting operation, we only use a few variables such as:

- `arrows`
- `end_point`
- `i`

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Intervals
- Array Traversal

---

## 🎯 Key Learning

- **Greedy and Sorting are different concepts**, but they are often used together.
- Sorting the intervals by their ending points allows us to make the best greedy decision.
- Placing the arrow at the **earliest ending point** maximizes the number of balloons that the same arrow can burst.
- We only need a new arrow when the next balloon starts **after** the current arrow position.
- When solving interval problems, sorting by either the **start** or **end** point can reveal useful greedy strategies.
