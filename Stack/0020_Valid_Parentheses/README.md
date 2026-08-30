# 🔗 Problem

Given a string `s` containing the characters:

```text
()
[]
{}
```

determine whether the string contains valid parentheses.

A string is valid if:

- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches the most recently opened bracket.

Return `True` if the string is valid, otherwise return `False`.

---

## 📝 Example

### Example 1

**Input**

```text
s = "()"
```

**Output**

```text
true
```

The parentheses are correctly opened and closed.

---

### Example 2

**Input**

```text
s = "()[]{}"
```

**Output**

```text
true
```

All brackets are correctly matched.

---

## 💡 Approach

### Stack

We use a **Stack** to keep track of opening brackets.

A stack follows:

> **LIFO — Last In, First Out**

This is perfect for parentheses because the most recently opened bracket must be the first one to close.

We create a dictionary:

```python
matches = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}
```

This tells us which opening bracket should match each closing bracket.

### When we find an opening bracket

We add it to the stack:

```python
stack.append(char)
```

### When we find a closing bracket

We check two things:

1. Is the stack empty?
2. Does the top of the stack match the required opening bracket?

```python
if not stack or stack[-1] != matches[char]:
    return False
```

If it matches, we remove the opening bracket:

```python
stack.pop()
```

After processing the entire string, the stack must be empty.

```python
return len(stack) == 0
```

If the stack is empty, every opening bracket has been properly closed.

---

## 🧠 Algorithm

1. Create an empty stack.
2. Create a dictionary containing matching opening brackets.
3. Traverse every character in `s`.
4. If the character is a closing bracket:
   - Check if the stack is empty.
   - Check if the top of the stack matches the corresponding opening bracket.
   - If not, return `False`.
   - Otherwise, remove the opening bracket using `pop()`.

5. If the character is an opening bracket, add it to the stack.
6. After traversing the entire string:
   - If the stack is empty, return `True`.
   - Otherwise, return `False`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- We traverse the string once.
- Each character is pushed onto or popped from the stack at most once.
- Dictionary lookup takes **O(1)** on average.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(n)**

In the worst case, all characters can be opening brackets.

For example:

```text
"((((((("
```

All of them would be stored in the stack.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Stack
- LIFO (Last In, First Out)
- Hash Map / Dictionary
- String Traversal
- Matching Brackets

---

## 🎯 Key Learning

- A **Stack** is useful whenever we need to process elements in **Last In, First Out** order.
- Parentheses naturally follow the LIFO pattern because the most recently opened bracket must close first.
- `append()` is used to **push** an element onto the stack.
- `pop()` is used to **remove the top element**.
- `stack[-1]` lets us look at the top element without removing it.
- The condition:

  ```python
  if not stack or stack[-1] != matches[char]:
  ```

  handles both an empty stack and an incorrect bracket match.

- This is a fundamental **Stack + Hash Map** problem and an important pattern to recognize for future DSA problems.
