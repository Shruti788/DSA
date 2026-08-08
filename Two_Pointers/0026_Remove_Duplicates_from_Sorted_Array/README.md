## 🔗 Problem

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique values in their original order.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [1,1,2]
```

**Output**

```text
2
```

The first two elements of `nums` become:

```text
[1,2]
```

---

### Example 2

**Input**

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Output**

```text
5
```

The first five elements of `nums` become:

```text
[0,1,2,3,4]
```

---

## 💡 Approach

### Two Pointers

Since the array is already sorted, all duplicate values are next to each other.

We use two pointers:

- `i` → slow pointer that keeps track of the position of the last unique element.
- `j` → fast pointer that scans through the array.

Initialize:

```python
i = 0
```

Then start `j` from index `1`.

For every element:

- If `nums[i] == nums[j]`, it is a duplicate, so we skip it.
- If `nums[i] != nums[j]`, we found a new unique element:
  - Move `i` forward.
  - Copy `nums[j]` to `nums[i]`.

At the end, the number of unique elements is:

```python
i + 1
```

---

## 🧠 Algorithm

1. Set `i = 0`.
2. Traverse the array using `j` from index `1`.
3. Compare `nums[i]` and `nums[j]`.
4. If they are different:
   - Increment `i`.
   - Set `nums[i] = nums[j]`.
5. Continue until `j` reaches the end.
6. Return `i + 1`.

---

## 🔍 Example Walkthrough

For:

```text
nums = [1,1,2,2,3]
```

Initially:

```text
i = 0
j = 1

[1,1,2,2,3]
 ↑ ↑
 i j
```

`nums[i] == nums[j]`, so `j` moves forward.

When `j` reaches `2`:

```text
[1,1,2,2,3]
 ↑   ↑
 i   j
```

Now:

```text
nums[i] != nums[j]
```

So:

```python
i += 1
nums[i] = nums[j]
```

Array becomes:

```text
[1,2,2,2,3]
   ↑
   i
```

The same process continues until the unique portion becomes:

```text
[1,2,3,...]
```

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

The array is traversed once using the `j` pointer.

Therefore:

**Time Complexity = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(1)**

No additional array or data structure is created.

The modification is performed **in-place**.

Therefore:

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Two Pointers
- Slow and Fast Pointers
- In-place Array Modification
- Sorted Arrays

---

## 🎯 Key Learning

Because the array is sorted, duplicates appear next to each other.

This allows us to efficiently remove duplicates without using a `set()` or another data structure.

The important pattern is:

```text
i → position for the next unique element
j → scans the array
```

This is a classic **Slow/Fast Pointer** technique that appears in many array problems.
