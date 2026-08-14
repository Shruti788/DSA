🔗 Problem

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character at most `k` times.

Return the length of the longest substring containing the same letter after performing at most `k` replacements.

---

## 📝 Example

### Example 1

**Input**

s = "ABAB"

k = 2

**Output**

4

---

### Example 2

**Input**

s = "AABABBA"

k = 1

**Output**

4

---

## 💡 Approach

### Sliding Window

We use a **variable-size sliding window** with two pointers:

- `left` → start of the window
- `right` → end of the window

We maintain a frequency dictionary `count` to store how many times each character appears in the current window.

We also maintain `max_frequency`, which represents the highest frequency of any character in the current window.

The number of replacements required to make the entire window contain the same character is:

window length - max frequency

In code:

(right - left + 1) - max_frequency

If the number of replacements required is greater than `k`, the window is invalid, so we shrink it from the left.

---

## ⏱ Complexity Analysis

### Time Complexity: O(n)

The `right` pointer moves through the string once, and the `left` pointer also moves forward at most `n` times.

Therefore, the overall time complexity is `O(n)`.

### Space Complexity: O(1)

The frequency dictionary contains at most 26 uppercase English letters, so the space used is constant.

---

## 📚 Concepts Used

- Sliding Window
- Two Pointers
- Hash Map / Dictionary
- Variable-Size Window
- String Traversal

---

## 🎯 Key Learning

The important pattern is:

Expand → update frequency → check replacements → Shrink if invalid → update maximum

The key formula is:

Window Length - Maximum Frequency <= k

If this condition is true, the current window is valid.

If it becomes false, we move the `left` pointer to shrink the window.S
