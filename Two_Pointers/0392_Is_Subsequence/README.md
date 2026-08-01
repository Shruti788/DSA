## 🔗 Problem

Given two strings `s` and `t`, determine whether `s` is a subsequence of `t`.

A subsequence is a sequence that can be derived from another string by deleting some or no characters without changing the relative order of the remaining characters.

Return `true` if `s` is a subsequence of `t`; otherwise, return `false`.

---

## 📝 Example

### Example 1

**Input**

```text
s = "abc"
t = "ahbgdc"
```

**Output**

```text
true
```

---

### Example 2

**Input**

```text
s = "axc"
t = "ahbgdc"
```

**Output**

```text
false
```

---

## 💡 Approach

### Two Pointers

Use two pointers to compare both strings.

- Initialize one pointer (`i`) for `s` and another pointer (`j`) for `t`.
- Traverse `t` from left to right.
- Whenever `s[i]` matches `t[j]`, move both pointers forward.
- Otherwise, move only the pointer in `t`.
- If all characters in `s` are matched, then `s` is a subsequence of `t`.

---

## 🧠 Algorithm

1. Initialize `i = 0` and `j = 0`.
2. While both pointers are within their string lengths:
   - If `s[i] == t[j]`, increment both pointers.
   - Otherwise, increment only `j`.
3. After the loop, check whether `i == len(s)`.
4. If true, all characters of `s` were matched; otherwise, return `False`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The pointer `j` traverses the string `t` once.
- The pointer `i` traverses the string `s` only when characters match.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = length of `t`

(Equivalently, you can write **O(n + m)**, where **m** is the length of `s`.)

---

### Space Complexity: **O(1)**

- Only two pointers are used.
- No extra data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- String Traversal

---

## 🎯 Key Learning

- The Two Pointers technique efficiently compares two strings while preserving character order.
- The pointer for the larger string (`t`) always moves forward, while the pointer for the smaller string (`s`) advances only when a match is found.
- If every character in `s` is matched in order, then `s` is a subsequence of `t`.
- This approach solves the problem in **O(n)** time without using extra space.
