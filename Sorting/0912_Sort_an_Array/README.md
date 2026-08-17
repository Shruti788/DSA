## 🔗 Problem

You are given an array of integers `nums`. Sort the array in ascending order and return the sorted array.

You must solve the problem without using built-in sorting functions.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [5,2,3,1]
```

**Output**

```text
[1,2,3,5]
```

---

### Example 2

**Input**

```text
nums = [5,1,1,2,0,0]
```

**Output**

```text
[0,0,1,1,2,5]
```

---

## 💡 Approach

### Merge Sort

Merge Sort uses the **Divide and Conquer** technique.

The main idea is to repeatedly divide the array into two smaller parts until each part contains only one element. A single element is already sorted.

Then, merge the smaller sorted arrays together while keeping the elements in ascending order.

For each pair of sorted arrays:

- Compare the current elements from the `left` and `right` arrays.
- Add the smaller element to the `result` array.
- Move the pointer of the array from which the element was taken.
- Continue until one of the arrays is completely processed.
- Add the remaining elements from the other array.

The function calls itself recursively using:

```python
left = self.sortArray(nums[:mid])
right = self.sortArray(nums[mid:])
```

Here, `self.sortArray()` applies the **same sorting function again** to the smaller left and right parts.

---

## 🧠 Algorithm

1. Check if the array contains `0` or `1` element.
   - If yes, return the array because it is already sorted.

2. Find the middle index using:

   ```python
   mid = len(nums) // 2
   ```

3. Divide the array into two halves:
   - `left = nums[:mid]`
   - `right = nums[mid:]`

4. Recursively sort both halves.
5. Initialize two pointers:
   - `i = 0` for the `left` array.
   - `j = 0` for the `right` array.

6. Compare `left[i]` and `right[j]`.
7. Add the smaller element to `result` and move its pointer forward.
8. After one side is completely processed, add all remaining elements from the other side.
9. Return the merged sorted `result` array.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n)**

- The array is repeatedly divided into two halves.
- Dividing the array creates approximately `log n` levels.
- At every level, all `n` elements are processed while merging.
- Therefore, the total time complexity is:

**Time Complexity = O(n log n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- The `result` arrays are created while merging.
- The recursive calls also use the call stack.
- The overall additional space required is proportional to the number of elements.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Merge Sort
- Recursion
- Divide and Conquer
- Two Pointers
- Array Traversal
- Merging Sorted Arrays

---
