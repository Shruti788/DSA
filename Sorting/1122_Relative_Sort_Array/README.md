# 🔗 Problem

Given two arrays `arr1` and `arr2`, sort the elements of `arr1` so that:

- The relative ordering of the elements that appear in `arr2` is the same as their ordering in `arr2`.
- Elements that do not appear in `arr2` are placed at the end of the array in **ascending order**.

Return the resulting sorted array.

---

## 📝 Example

### Example 1

**Input**

```text
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
```

**Output**

```text
[2,2,2,1,4,3,3,9,6,7,19]
```

---

### Example 2

**Input**

```text
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
```

**Output**

```text
[22,28,8,6,17,44]
```

---

## 💡 Approach

### Frequency Count + Sorting

We first create a dictionary called `count` to store how many times each number appears in `arr1`.

For example:

```text
arr1 = [2,2,2,1,4,3,3]
```

The dictionary becomes:

```text
{
    2: 3,
    1: 1,
    4: 1,
    3: 2
}
```

Then:

- Traverse `arr2`.
- For every number in `arr2`, add it to `result` as many times as it appears in `arr1`.
- Next, find the numbers that are present in `arr1` but **not** in `arr2`.
- Store those numbers in `remaining`.
- Sort `remaining` in ascending order.
- Finally, append `remaining` to `result`.

This ensures that the elements from `arr2` follow the required relative order, while all other elements are sorted normally.

---

## 🧠 Algorithm

1. Create an empty dictionary `count`.
2. Traverse `arr1` and count the frequency of every number.
3. Create an empty list `result`.
4. Traverse `arr2`:
   - Find how many times the current number appears in `arr1`.
   - Add that number to `result` that many times.

5. Create an empty list `remaining`.
6. Traverse the keys of `count`:
   - If the number is not present in `arr2`, add it to `remaining` according to its frequency.

7. Sort `remaining` in ascending order.
8. Extend `result` with `remaining`.
9. Return `result`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n + m + k log k)**

Let:

- `n` = length of `arr1`

- `m` = length of `arr2`

- `k` = number of elements in `remaining`

- Creating the frequency dictionary takes **O(n)**.

- Traversing `arr2` takes **O(m)**.

- Building `remaining` takes **O(n)** in the worst case.

- Sorting `remaining` takes **O(k log k)**.

Therefore,

**Time Complexity = O(n + m + k log k)**

---

### Space Complexity: **O(n)**

- The `count` dictionary stores the frequency of elements from `arr1`.
- The `result` and `remaining` lists also require additional space.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Hash Map / Dictionary
- Frequency Counting
- Array Traversal
- Sorting
- Lists
- Two-Array Processing

---

## 🎯 Key Learning

- A **dictionary** can be used to efficiently count how many times each element appears.
- When one array determines the required order, process that array first and use the frequency information from the other array.
- The `for _ in range(count[num])` loop is useful when we need to add an element multiple times based on its frequency.
- Elements that are not present in `arr2` can be collected separately and sorted before being added to the final result.
- This problem is a good example of combining **Hash Maps + Sorting** to control the order of elements efficiently.
