# 217. Contains Duplicate

## Approach

- Hash Set

A set stores only unique values.

- Create an empty set.
- Traverse the array.
- If the current element already exists in the set, a duplicate is found.
- Return `True`.
- Otherwise, insert the element into the set.
- If the loop finishes, return `False`.

## Time Complexity

- O(n)

## Space Complexity

- O(n)
