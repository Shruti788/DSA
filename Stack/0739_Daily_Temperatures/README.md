# 🔗 Problem

Given an array `temperatures` representing the daily temperatures, return an array `answer` such that:

`answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature.

If there is no future day with a warmer temperature, `answer[i] = 0`.

---

## 📝 Example

### Example 1

**Input:**

```text
temperatures = [73,74,75,71,69,72,76,73]
```

**Output:**

```text
[1,1,4,2,1,1,0,0]
```

**Explanation:**

- 73 → 74 → wait 1 day
- 74 → 75 → wait 1 day
- 75 → 76 → wait 4 days
- 71 → 72 → wait 2 days
- 69 → 72 → wait 1 day
- 72 → 76 → wait 1 day
- 76 → no warmer day → 0
- 73 → no warmer day → 0

---

### Example 2

**Input:**

```text
temperatures = [30,40,50,60]
```

**Output:**

```text
[1,1,1,0]
```

---

## 💡 Approach

We use a **Monotonic Stack**.

The stack stores the **indices** of days whose warmer temperature has not been found yet.

For every temperature:

1. Check the top index of the stack.
2. If the current temperature is warmer than the temperature at that index:
   - Pop that index.
   - Calculate how many days we waited:

     ```python
     i - prev
     ```

   - Store this value in `ans[prev]`.

3. Continue checking the stack.
4. Push the current index into the stack.

We store **indices**, not temperatures, because we need the difference between the current day and the previous day.

---

## 🧠 Algorithm

```text
Create an empty stack
Create an answer array filled with 0

For each index i:

    While stack is not empty
    AND current temperature > temperature at stack top:

        prev = pop the stack

        answer[prev] = i - prev

    Push i into the stack

Return answer
```

---

## ⏱ Complexity Analysis

### Time Complexity

```text
O(n)
```

Each index is pushed onto the stack once and popped at most once.

### Space Complexity

```text
O(n)
```

The stack and answer array can contain up to `n` elements.

---

## 📚 Concepts Used

- Stack
- Monotonic Stack
- Array
- Index Tracking
- Next Greater Element Pattern

---

## 🎯 Key Learning

This problem is essentially a variation of the **Next Greater Element** pattern.

In LeetCode 496, we asked:

> "What is the next greater number?"

Here, we ask:

> "How many days until the next greater temperature?"

The important difference is that we store **indices** in the stack:

```python
stack.append(i)
```

This allows us to calculate the number of days:

```python
ans[prev] = i - prev
```

### ⭐ Important Pattern

```python
while stack and temperatures[i] > temperatures[stack[-1]]:
    prev = stack.pop()
    ans[prev] = i - prev
```

Whenever the current element is greater than the element represented by the stack's top index, **we have found its next greater element**.

This same Monotonic Stack pattern appears in many problems involving:

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element
- Daily Temperatures
