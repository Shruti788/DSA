# 125. Valid Palindrome

## 🔗 Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## 📝 Example

### Example 1

**Input**

```text
s = "A man, a plan, a canal: Panama"
```

**Output**

```text
true
```

**Explanation**

After removing non-alphanumeric characters and converting to lowercase:

```text
"amanaplanacanalpanama"
```

which reads the same forward and backward.

---

### Example 2

**Input**

```text
s = "race a car"
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
s = " "
```

**Output**

```text
true
```

---

## 💡 Approach

### Two Pointers

Use two pointers to compare characters from both ends of the string.

- Initialize one pointer at the beginning (`left`) and one at the end (`right`).
- Skip characters that are not letters or digits using `isalnum()`.
- Convert both characters to lowercase before comparing them.
- If the characters are different, return `False`.
- Otherwise, move both pointers toward the center.
- If all valid characters match, return `True`.

---

## 🧠 Algorithm

1. Initialize `left = 0` and `right = len(s) - 1`.
2. While `left < right`:
   - If `s[left]` is not alphanumeric, increment `left`.
   - Else if `s[right]` is not alphanumeric, decrement `right`.
   - Else compare both characters after converting them to lowercase.
   - If they are different, return `False`.
   - Otherwise, move both pointers inward.
3. Return `True`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Each character is visited at most once by either the `left` or `right` pointer.
- The pointers move only toward the center of the string.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = length of the string.

---

### Space Complexity: **O(1)**

- No extra data structures are used.
- Only two pointer variables are maintained.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- String Traversal
- Character Manipulation
- Case Conversion
- Alphanumeric Check

---

## 🎯 Key Learning

- The **Two Pointers** technique is an efficient way to compare elements from both ends of a sequence.
- Functions like `isalnum()` help ignore non-alphanumeric characters.
- Using `lower()` makes the comparison case-insensitive.
- This approach avoids creating a new filtered string and solves the problem using constant extra space.

---

## 🏷️ Tags

`String` `Two Pointers` `Palindrome`