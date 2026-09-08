# 🔗 Problem

**LeetCode 496 — Next Greater Element I**

You are given two arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element in `nums1`, find the **next greater element** in `nums2`.

The next greater element of an element `x` is the first element to the right of `x` that is greater than `x`.

If there is no greater element, return `-1`.

---

## 📝 Example

### Example 1

**Input:**

```text
nums1 = [4,1,2]
nums2 = [1,3,4,2]
```

**Output:**

```text
[-1,3,-1]
```

**Explanation:**

- For `4`: there is no greater element → `-1`
- For `1`: next greater element is `3`
- For `2`: there is no greater element → `-1`

---

### Example 2

**Input:**

```text
nums1 = [2,4]
nums2 = [1,2,3,4]
```

**Output:**

```text
[3,-1]
```

**Explanation:**

- For `2`: next greater element is `3`
- For `4`: there is no greater element → `-1`

---

## 💡 Approach

We use a **Monotonic Stack** and a **Hash Map**.

### Step 1: Process `nums2`

We maintain a stack containing elements for which we have not found a greater element yet.

For every number `num` in `nums2`:

- While the stack is not empty and `num` is greater than the top element:
  - Remove the smaller element from the stack.
  - Store `num` as its next greater element in the dictionary.

- Push `num` into the stack.

### Step 2: Build the answer

Now that we know the next greater element for every possible number in `nums2`, we simply look up each number from `nums1`.

If the number is not present in `greater`, we return `-1`.

---

## 🧠 Algorithm

```text
Create an empty stack
Create an empty dictionary greater

For every number in nums2:

    While stack is not empty AND current number > stack top:
        smaller = pop from stack
        greater[smaller] = current number

    Push current number into stack

Create an empty answer list

For every number in nums1:
    Add greater[number] if it exists
    Otherwise add -1

Return answer
```

---

## ⏱ Complexity Analysis

### Time Complexity

```text
O(n + m)
```

- `n` = length of `nums2`
- `m` = length of `nums1`

Every element in `nums2` is pushed and popped from the stack at most once.

### Space Complexity

```text
O(n)
```

The stack and dictionary can contain up to `n` elements.

---

## 📚 Concepts Used

- Stack
- Monotonic Stack
- Hash Map / Dictionary
- Next Greater Element
- LIFO (Last In, First Out)

---

## 🎯 Key Learning

The important idea is the **Monotonic Stack**.

Instead of checking every element to the right of each number, we process `nums2` once and keep track of numbers waiting for their next greater element.

The key pattern is:

```python
while stack and num > stack[-1]:
    smaller = stack.pop()
    greater[smaller] = num
```

When the current number is greater than the stack's top, we have just found the **next greater element** for that smaller number.

This pattern is extremely useful for problems involving:

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element
- Temperature-style problems
