## 🔗 Problem

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`.

A permutation contains the **same characters with the same frequencies**, but the characters can appear in a different order.

---

## 📝 Example

### Example 1

**Input:**

```text
s1 = "ab"
s2 = "eidbaooo"
```

**Output:**

```text
True
```

**Explanation:**

`s2` contains `"ba"`, which is a permutation of `"ab"`.

---

### Example 2

**Input:**

```text
s1 = "ab"
s2 = "eidboaoo"
```

**Output:**

```text
False
```

---

## 💡 Approach

We use the **Sliding Window** technique.

The idea is:

1. Count the frequency of every character in `s1`.
2. Create a window in `s2` with the same length as `s1`.
3. Keep track of the character frequencies inside the current window.
4. If the window's frequency dictionary matches the target dictionary, a permutation exists.
5. Move the window forward by:
   - Adding the new character on the right.
   - Removing the character that goes out from the left.

---

## ⏱️ Complexity

### Time Complexity

```text
O(n)
```

where `n` is the length of `s2`.

We move the `right` and `left` pointers through the string without repeatedly scanning the entire string.

### Space Complexity

```text
O(k)
```

where `k` is the number of distinct characters stored in the dictionaries.

For lowercase English letters, this is effectively:

```text
O(26)
```

which is considered:

```text
O(1)
```

---

## 🧩 Pattern Learned

**Sliding Window + Hash Map**

This problem is useful for learning how to:

- Track character frequencies.
- Maintain a fixed-size window.
- Move `left` and `right` pointers.
- Add and remove elements from a window.
- Compare frequency maps.

---

## 📌 Key Takeaway

The main idea is:

> **Keep a window of the same length as `s1` and check whether its character frequencies match `s1`.**

Instead of checking every possible substring from scratch, we update the existing window as it moves.

That makes the solution efficient with **O(n) time complexity**.
