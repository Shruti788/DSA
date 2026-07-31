## 🔗 Problem

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.

---

## 📝 Example

### Example 1

**Input**

```text
s = "abcabcbb"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is `"abc"`.

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

The longest substring without repeating characters is `"b"`.

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is `"wke"`.

---

## 💡 Approach

### Sliding Window

Use a variable-size sliding window to maintain a substring containing only unique characters.

- Use a set to store the characters currently inside the window.
- Expand the window by moving the `right` pointer.
- If a duplicate character is found, repeatedly remove characters from the left side of the window until the duplicate is removed.
- Add the current character to the set.
- Update the maximum window length after every iteration.

This ensures that the window always contains unique characters.

---

## 🧠 Algorithm

1. Create an empty set `seen`.
2. Initialize `left = 0` and `max_length = 0`.
3. Traverse the string using `right`.
4. While the current character already exists in the set:
   - Remove `s[left]` from the set.
   - Increment `left`.
5. Add the current character to the set.
6. Update the maximum length using:

```python
right - left + 1
```

7. Return `max_length`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Each character is added to the set at most once.
- Each character is removed from the set at most once.
- Therefore, each character is processed a constant number of times.

**Time Complexity = O(n)**

where:

- **n** = length of the string.

---

### Space Complexity: **O(min(n, m))**

- The set stores only the unique characters currently in the sliding window.
- In the worst case, the window contains all unique characters.
- If the character set is limited (e.g., English letters), the space is bounded by the number of unique characters `m`.

Therefore,

**Space Complexity = O(min(n, m))**

---

## 📚 Concepts Used

- Sliding Window
- Hash Set
- String Traversal
- Two Pointers

---

## 🎯 Key Learning

- A variable-size sliding window allows us to efficiently maintain a substring that satisfies a condition.
- A hash set provides constant-time lookup to detect duplicate characters.
- Shrinking the window only when necessary ensures each character is processed efficiently.
- This approach improves the brute-force **O(n²)** solution to an optimal **O(n)** solution.
