# 🔗 Problem

You are given a list of operations representing a baseball game.

Each operation can be one of the following:

- An integer → Add that score to the record.
- `"C"` → Invalidate the previous score and remove it.
- `"D"` → Add a score equal to **double the previous score**.
- `"+"` → Add a score equal to the **sum of the previous two scores**.

Return the total score after performing all operations.

---

## 📝 Example

### Example 1

**Input**

```text
operations = ["5","2","C","D","+"]
```

**Output**

```text
30
```

**Explanation**

Process the operations:

```text
"5" → [5]
"2" → [5, 2]
"C" → [5]
"D" → [5, 10]
"+" → [5, 10, 15]
```

Final score:

```text
5 + 10 + 15 = 30
```

---

## 💡 Approach

### Stack

We use a **Stack** to store all valid scores.

A stack is useful because several operations depend on the **most recent scores**.

We initialize:

```python
stack = []
```

### Integer

If the operation is a number, convert it from a string to an integer and add it to the stack:

```python
stack.append(int(op))
```

### `"C"`

`"C"` means cancel the previous score.

So we remove the last score:

```python
stack.pop()
```

### `"D"`

`"D"` means double the previous score.

The previous score is at the top of the stack:

```python
stack[-1]
```

So:

```python
stack.append(stack[-1] * 2)
```

### `"+"`

`"+"` means add the previous two scores.

The last score is:

```python
stack[-1]
```

The second-last score is:

```python
stack[-2]
```

Therefore:

```python
stack.append(stack[-1] + stack[-2])
```

Finally, we add all valid scores:

```python
return sum(stack)
```

The key idea is:

> **Use the stack to always keep track of the valid scores needed by future operations.**

---

## 🧠 Algorithm

1. Create an empty stack.
2. Traverse every operation.
3. If the operation is an integer:
   - Convert it to an integer.
   - Push it onto the stack.

4. If the operation is `"C"`:
   - Remove the previous score using `pop()`.

5. If the operation is `"D"`:
   - Double the last score and push the result.

6. If the operation is `"+"`:
   - Add the last two scores and push the result.

7. Return the sum of all scores in the stack.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

We process every operation once.

The final `sum(stack)` also takes O(n).

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(n)**

In the worst case, every operation can add a score to the stack.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Stack
- LIFO (Last In, First Out)
- Array Traversal
- String Processing
- `append()`
- `pop()`

---

## 🎯 Key Learning

- A **Stack** is useful when a problem repeatedly asks about the most recent elements.
- `stack[-1]` gives the **last/current score**.
- `stack[-2]` gives the **second-last score**.
- `append()` adds a new score.
- `pop()` removes the most recent score.
- Different operations can be handled by modifying the stack directly.
- This is a great beginner problem for understanding how stacks can maintain **history/state** while processing a sequence of operations.
