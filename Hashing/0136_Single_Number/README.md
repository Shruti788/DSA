## 🔗 Problem

Given a **non-empty** array of integers `nums`, every element appears **twice** except for one. Find that single element.

You must return the element that appears only once.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [2,2,1]
```

**Output**

```text
1
```

---

### Example 2

**Input**

```text
nums = [4,1,2,1,2]
```

**Output**

```text
4
```

---

### Example 3

**Input**

```text
nums = [1]
```

**Output**

```text
1
```

---

## 💡 Approach

### Hash Map (Dictionary)

Use a dictionary to count the frequency of each number.

- Traverse the array and store the frequency of every element.
- Traverse the dictionary.
- Return the number whose frequency is equal to `1`.

Since the problem guarantees that exactly one element appears only once, the algorithm will always find the correct answer.

---

## 🧠 Algorithm

1. Create an empty dictionary called `freq`.
2. Traverse the array.
3. If the number already exists in the dictionary, increase its frequency.
4. Otherwise, add it to the dictionary with a frequency of `1`.
5. Traverse the dictionary using `freq.items()`.
6. Return the key whose frequency is equal to `1`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The first loop traverses the array once to count the frequency of each element, which takes **O(n)** time.
- The second loop traverses the dictionary to find the element with a frequency of `1`, which takes **O(n)** time in the worst case.

Therefore,

**Total Time Complexity = O(n) + O(n) = O(n)**

where:

- **n** = number of elements in the array.

---

### Space Complexity: **O(n)**

- The dictionary stores the frequency of each unique element.
- In the worst case, all elements are unique, requiring **O(n)** extra space.

Therefore,

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Hash Map (Dictionary)
- Frequency Counting
- Array Traversal
