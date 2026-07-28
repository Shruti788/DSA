## 🔗 Problem

Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**.

Each element in the result **must be unique**, and you may return the result in any order.

---

## 💡 Approach

### Hash Set

A **Hash Set** provides fast lookup in **O(1)** average time.

1. Convert `nums2` into a set.
2. Create an empty set called `result`.
3. Traverse every element in `nums1`.
4. If the current element exists in `nums2_set`, add it to `result`.
5. Convert the result set into a list and return it.

Using a set automatically removes duplicate values from the final answer.

---

### Time Complexity: **O(n + m)**

- Creating a Hash Set from `nums2` takes **O(m)** time.
- Iterating through `nums1` takes **O(n)** time.
- Checking whether an element exists in a Hash Set takes **O(1)** average time.

Therefore,

**Total Time Complexity = O(m) + O(n) = O(n + m)**

where:

- **n** = length of `nums1`
- **m** = length of `nums2`

---

### Space Complexity: **O(m)**

- The Hash Set `nums2_set` stores all unique elements from `nums2`, requiring **O(m)** extra space.
- The `result` set stores only the intersection elements. In the worst case, it can contain up to `min(n, m)` unique elements.

Therefore, the overall auxiliary space complexity is **O(m)**.
