## 🔗 Problem

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`.

If one string is longer than the other, append the remaining letters to the end of the merged string.

Return the merged string.

---

## 📝 Example

### Example 1

**Input**

```text
word1 = "abc"
word2 = "pqr"
```

**Output**

```text
"apbqcr"
```

---

### Example 2

**Input**

```text
word1 = "ab"
word2 = "pqrs"
```

**Output**

```text
"apbqrs"
```

---

### Example 3

**Input**

```text
word1 = "abcd"
word2 = "pq"
```

**Output**

```text
"apbqcd"
```

---

## 💡 Approach

### Two Pointers

Use two pointers to traverse both strings simultaneously.

- Initialize one pointer for `word1` and another for `word2`.
- While both pointers are within their respective strings:
  - Append one character from `word1`.
  - Append one character from `word2`.
- After one string is exhausted, append the remaining characters from the other string.
- Finally, join the list of characters into a single string.

---

## 🧠 Algorithm

1. Initialize `left = 0` and `right = 0`.
2. Create an empty list `result`.
3. While both pointers are within their string lengths:
   - Append `word1[left]`.
   - Increment `left`.
   - Append `word2[right]`.
   - Increment `right`.
4. Append any remaining characters from `word1`.
5. Append any remaining characters from `word2`.
6. Return `"".join(result)`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n + m)**

- The first loop processes characters from both strings until one is exhausted.
- The remaining loops process any leftover characters.
- Each character from both strings is visited exactly once.

Therefore,

**Time Complexity = O(n + m)**

where:

- **n** = length of `word1`
- **m** = length of `word2`

---

### Space Complexity: **O(n + m)**

- The `result` list stores all characters from both strings.
- The final merged string is created by joining the list.

Therefore,

**Space Complexity = O(n + m)**

---

## 📚 Concepts Used

- Two Pointers
- String Traversal
- String Manipulation
- List Operations

---

## 🎯 Key Learning

- The **Two Pointers** technique can be applied to strings as well as arrays.
- Building the result using a list and then using `"".join()` is more efficient than repeatedly concatenating strings.
- Handling the remaining characters after one string is exhausted ensures all characters are included in the final result.
