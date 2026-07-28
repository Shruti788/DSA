## 🔗 Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Approach

- Hash Map (Dictionary)

A dictionary keeps track of how many times each character appears.

- If the lengths are different, they cannot be anagrams.
- Count the frequency of every character in the first string.
- Decrease the frequency while traversing the second string.
- If any character is missing or the counts don't match, return `False`.
- If all frequencies become zero, return `True`.

## Time Complexity

- O(n)

## Space Complexity

- O(n)
