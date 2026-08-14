## 🔗 Problem

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

You may return the answer in any order.

An anagram contains the same characters with the same frequencies, but the characters can appear in a different order.

---

## 📝 Example

### Example 1

**Input**

```text
s = "cbaebabacd"
p = "abc"
```

**Output**

```text
[0,6]
```

Explanation:

The substring starting at index `0` is:

```text
"cba"
```

which is an anagram of `"abc"`.

The substring starting at index `6` is:

```text
"bac"
```

which is also an anagram of `"abc"`.

---

### Example 2

**Input**

```text
s = "abab"
p = "ab"
```

**Output**

```text
[0,1,2]
```

The anagrams are:

```text
"ab" → index 0
"ba" → index 1
"ab" → index 2
```

---

## 💡 Approach — Sliding Window + Hash Map

We need to find every substring of `s` that is an anagram of `p`.

Since every anagram of `p` has exactly the same length as `p`, we use a **fixed-size sliding window**.

The window size is:

```python
len(p)
```

We use two dictionaries:

```python
target = {}
window = {}
```

### `target`

Stores the frequency of each character in `p`.

For example:

```text
p = "abc"
```

gives:

```python
target = {
    'a': 1,
    'b': 1,
    'c': 1
}
```

### `window`

Stores the frequency of characters inside the current window of `s`.

Whenever the window becomes larger than `len(p)`, we remove the character at the left side.

Whenever:

```python
window == target
```

the current window is an anagram of `p`, so we add its starting index to `result`.

---

## 🧠 Algorithm

1. Create a frequency map `target` for string `p`.
2. Create an empty frequency map `window`.
3. Create an empty list `result`.
4. If `p` is longer than `s`, return `result`.
5. Use `left` and `right` pointers to maintain a fixed-size window.
6. Add `s[right]` to `window`.
7. If the window becomes larger than `len(p)`:
   - Remove `s[left]`.
   - Delete the character from the dictionary if its frequency becomes `0`.
   - Move `left` forward.
8. Compare `window` with `target`.
9. If they are equal, append `left` to `result`.
10. Return `result`.

---

## 🔍 Dry Run

Consider:

```text
s = "cbaebabacd"
p = "abc"
```

The target frequency is:

```python
target = {
    'a': 1,
    'b': 1,
    'c': 1
}
```

The window size must always be:

```text
3
```

### First Window

```text
"cba"
```

Frequency:

```python
{
    'c': 1,
    'b': 1,
    'a': 1
}
```

This matches `target`.

Therefore:

```text
result = [0]
```

---

The window continues moving through the string.

When we reach:

```text
"bac"
```

at index `6`, its frequency also matches `target`.

Therefore:

```text
result = [0,6]
```

Final answer:

```text
[0,6]
```

---

## ⏱ Complexity Analysis

### Time Complexity: O(n)

We traverse `s` once using the sliding window.

The `left` pointer also moves forward at most `n` times.

Therefore:

```text
O(n)
```

where `n` is the length of `s`.

---

### Space Complexity: O(1)

The `target` and `window` dictionaries store character frequencies.

With a fixed character set, the number of possible characters is bounded.

Therefore:

```text
O(1)
```

---

## 📚 Concepts Used

- Sliding Window
- Fixed-Size Window
- Hash Map
- Frequency Counting
- Two Pointers
- String Traversal

---

## 🎯 Key Learning

Anagrams have the same character frequencies.

Instead of generating every possible substring and sorting it, we maintain a fixed-size window and compare its frequency map with the frequency map of `p`.
