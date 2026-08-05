## 🔗 Problem

Given two strings `s` and `t`, determine if they are **isomorphic**.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`.

- Every character must map to exactly one character.
- No two different characters can map to the same character.
- A character may map to itself.

Return `true` if the strings are isomorphic; otherwise, return `false`.

---

## 📝 Example

### Example 1

**Input**

```text
s = "egg"
t = "add"
```

**Output**

```text
true
```

---

### Example 2

**Input**

```text
s = "foo"
t = "bar"
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
s = "paper"
t = "title"
```

**Output**

```text
true
```

---

## 💡 Approach

### Hash Map

Use two hash maps to maintain a one-to-one mapping:

- `mapST` stores the mapping from characters in `s` to characters in `t`.
- `mapTS` stores the reverse mapping from `t` to `s`.

For every character pair:

- If the mapping already exists, verify that it is consistent.
- Otherwise, create the mapping.
- Repeat the same process in the reverse direction.
- If any inconsistency is found, return `False`.

If the entire string is processed without conflicts, return `True`.

---

## 🧠 Algorithm

1. If the lengths of the strings are different, return `False`.
2. Create two empty dictionaries:
   - `mapST`
   - `mapTS`
3. Traverse both strings simultaneously.
4. Check the mapping from `s` to `t`.
5. Check the reverse mapping from `t` to `s`.
6. If any mapping conflicts, return `False`.
7. If all mappings are valid, return `True`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- Traverse both strings once.
- Dictionary lookups and insertions take **O(1)** on average.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = length of the strings.

---

### Space Complexity: **O(n)**

- In the worst case, each unique character is stored in both dictionaries.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Hash Map
- String Traversal
- Character Mapping

---

## 🎯 Key Learning

- A single hash map is not sufficient because multiple characters could incorrectly map to the same character.
- Using two hash maps guarantees a one-to-one correspondence (bijection) between characters.
- Verifying both forward and reverse mappings ensures the strings are truly isomorphic.
