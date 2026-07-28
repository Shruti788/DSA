## 🔗 Problem

Given an integer array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the majority element always exists in the array.

---

## 💡 Approach

### Hash Map (Dictionary)

A dictionary is used to count the frequency of every number in the array.

1. Create an empty dictionary called `freq`.
2. Traverse the array.
3. If the element already exists in the dictionary, increase its count.
4. Otherwise, add it with a frequency of `1`.
5. Traverse the dictionary using `freq.items()`.
6. If any element appears more than `len(nums) / 2` times, return that element.

Since the problem guarantees that a majority element always exists, the algorithm will always return a valid answer.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The first loop traverses the array once to count the frequency of each element, which takes **O(n)** time.
- The second loop traverses the dictionary. In the worst case, the dictionary contains all unique elements, which also takes **O(n)** time.

Therefore,

**Total Time Complexity = O(n) + O(n) = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- The dictionary stores the frequency of each unique element.
- In the worst case, every element is unique, so the dictionary stores **n** entries.

Therefore,

**Space Complexity = O(n)**
