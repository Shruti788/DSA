## 🔗 Problem

Write a function that reverses a string.

The input is given as an array of characters `s`.

You must modify the input array **in-place** with **O(1)** extra memory.

---

## 📝 Example

### Example 1

**Input**

```text
s = ["h","e","l","l","o"]
```

**Output**

```text
["o","l","l","e","h"]
```

---

### Example 2

**Input**

```text
s = ["H","a","n","n","a","h"]
```

**Output**

```text
["h","a","n","n","a","H"]
```

---

## 💡 Approach

### Two Pointers

Use two pointers:

- `left` starts at the beginning of the array.
- `right` starts at the end of the array.

While `left < right`:

- Swap the characters at both pointers.
- Move `left` one step forward.
- Move `right` one step backward.

Continue until the pointers meet.

Since the array is modified directly, no extra array is required.

---

## 🧠 Algorithm

1. Initialize:
   - `left = 0`
   - `right = len(s) - 1`
2. While `left < right`:
   - Swap `s[left]` and `s[right]`.
   - Increment `left`.
   - Decrement `right`.
3. The array is now reversed in place.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Each character is swapped at most once.
- The pointers move toward the center.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = length of the character array.

---

### Space Complexity: **O(1)**

- Only two pointer variables are used.
- The reversal is performed in-place.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- In-place Modification
- Array Traversal
- Swapping

---

## 🎯 Key Learning

- Two pointers can efficiently reverse an array or string in a single pass.
- Swapping elements in-place avoids using additional memory.
- This is a fundamental technique used in many array and string interview problems.
