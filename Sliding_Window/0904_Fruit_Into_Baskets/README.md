## 🔗 Problem

You are given an integer array `fruits` where `fruits[i]` represents the type of fruit on the `i-th` tree.

You have **two baskets**, and each basket can hold only **one type of fruit**.

Starting from any tree, you must pick exactly one fruit from every tree while moving to the right.

Return the **maximum number of fruits** you can collect.

In other words, find the length of the **longest contiguous subarray containing at most 2 distinct values**.

---

## 📝 Example

### Example 1

**Input**

```text
fruits = [1, 2, 1]
```

**Output**

```text
3
```

**Explanation**

We can collect:

```text
[1, 2, 1]
```

There are only 2 different types of fruits, so we can collect all 3 fruits.

---

### Example 2

**Input**

```text
fruits = [0, 1, 2, 2]
```

**Output**

```text
3
```

---

## 💡 Approach

This problem can be solved using the **Sliding Window** technique.

We maintain a window between two pointers:

```text
left
  ↓
[ ... window ... ]
              ↑
            right
```

The window is valid when it contains **at most 2 distinct fruit types**.

We use a dictionary called `count` to store the frequency of each fruit inside the current window.

### Steps

1. Start with:
   - `left = 0`
   - `max_length = 0`
   - `count = {}`

2. Move `right` through the array.

3. Add `fruits[right]` to the dictionary.

4. If the window contains more than 2 distinct fruit types:

```python
while len(count) > 2:
```

Move `left` forward and decrease the frequency of `fruits[left]`.

5. If a fruit's frequency becomes `0`, remove it from the dictionary.

6. Once the window becomes valid again, calculate its length:

```python
right - left + 1
```

7. Keep track of the maximum window length.

---

## 🔍 Dry Run

Consider:

```text
fruits = [1, 2, 3, 2, 2]
```

### Step 1

```text
right = 0
fruit = 1
```

```text
count = {1: 1}
```

Window:

```text
[1]
```

Length:

```text
1
```

`max_length = 1`

---

### Step 2

```text
right = 1
fruit = 2
```

```text
count = {1: 1, 2: 1}
```

Window:

```text
[1, 2]
```

Length:

```text
2
```

`max_length = 2`

---

### Step 3

```text
right = 2
fruit = 3
```

```text
count = {1: 1, 2: 1, 3: 1}
```

Now we have **3 different fruit types**, which is invalid.

So we move `left`.

Remove fruit `1`:

```text
count = {2: 1, 3: 1}
left = 1
```

Window becomes:

```text
[2, 3]
```

Length:

```text
2
```

---

### Step 4

```text
right = 3
fruit = 2
```

```text
count = {2: 2, 3: 1}
```

Window:

```text
[2, 3, 2]
```

Length:

```text
3
```

`max_length = 3`

---

### Step 5

```text
right = 4
fruit = 2
```

```text
count = {2: 3, 3: 1}
```

Window:

```text
[2, 3, 2, 2]
```

Length:

```text
4
```

`max_length = 4`

Final answer:

```text
4
```

---

## ⏱️ Complexity

### Time Complexity

```text
O(n)
```

Each element is added to the window once and removed from the window at most once.

### Space Complexity

```text
O(1)
```

The dictionary stores at most **3 fruit types temporarily** before the window is shrunk back to 2.

---

## 🧠 Key Pattern

This is a classic **Variable Size Sliding Window** problem.
