## 🔗 Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using the letters from `magazine`.

Each letter in `magazine` can only be used once in `ransomNote`.

Return `false` otherwise.

---

## 📝 Example

### Example 1

**Input**

```text
ransomNote = "a"
magazine = "b"
```

**Output**

```text
false
```

---

### Example 2

**Input**

```text
ransomNote = "aa"
magazine = "ab"
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
ransomNote = "aa"
magazine = "aab"
```

**Output**

```text
true
```

---

## 💡 Approach

### Hash Map (Frequency Count)

Use a hash map to store the frequency of each character in `magazine`.

- Traverse `magazine` and count the occurrences of every character.
- Traverse `ransomNote`.
- For each character:
  - If the character does not exist in the hash map, return `False`.
  - Decrease its frequency by one.
  - If the frequency becomes negative, return `False` because the character has been used more times than available.
- If all characters are successfully matched, return `True`.

---

## 🧠 Algorithm

1. Create an empty dictionary `freq`.
2. Traverse `magazine` and store the frequency of each character.
3. Traverse `ransomNote`.
4. For each character:
   - If it is not present in `freq`, return `False`.
   - Decrease its frequency.
   - If its frequency becomes negative, return `False`.
5. If all characters are processed successfully, return `True`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(m + n)**

- Building the frequency map takes **O(m)**.
- Traversing the ransom note takes **O(n)**.

Overall,

**Time Complexity = O(m + n)**

where:

- **m** = length of `magazine`
- **n** = length of `ransomNote`

---

### Space Complexity: **O(k)**

- The dictionary stores the frequency of unique characters.

where:

- **k** = number of unique characters in `magazine`.

In the worst case, this is **O(m)**.

---

## 📚 Concepts Used

- Hash Map
- Frequency Counting
- String Traversal

---

## 🎯 Key Learning

- A frequency hash map is useful when tracking how many times each element appears.
- By decrementing the count as characters are used, we can efficiently determine whether enough characters are available.
- This avoids repeatedly searching through the string and improves the solution from **O(m × n)** to **O(m + n)**.
