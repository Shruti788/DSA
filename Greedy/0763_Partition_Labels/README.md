# 🔗 Problem

You are given a string `s`.

You want to partition the string into as many parts as possible so that **each letter appears in at most one part**.

After partitioning, concatenate all the parts together to form the original string.

Return a list containing the **size of each partition**.

---

### Example

**Input**

```text
s = "ababcbacadefegdehijhklij"
```

**Output**

```text
[9,7,8]
```

**Explanation**

The string can be partitioned into:

```text
"ababcbaca" "defegde" "hijhklij"
```

The sizes of these partitions are:

```text
9, 7, 8
```

## Each letter appears in only one partition.

## 💡 Approach

### Greedy + Hash Map

First, we store the **last occurrence** of every character in the string.

```python
last = {}

for i in range(len(s)):
    last[s[i]] = i
```

For example, for:

```text
s = "ababcbacadefegdehijhklij"
```

`last` stores the final index where each character appears.

Then we traverse the string again.

We maintain:

```python
start = 0
end = 0
```

- `start` represents the beginning of the current partition.
- `end` represents the farthest position the current partition must reach.

For every character, we update `end`:

```python
end = max(end, last[s[i]])
```

This is important because if a character appears again later, the current partition must extend to include its last occurrence.

Once:

```python
i == end
```

we know that every character in the current partition has its last occurrence inside this partition.

Therefore, we can safely create a partition:

```python
result.append(end - start + 1)
```

Then start the next partition:

```python
start = i + 1
```

The greedy idea is:

> **Extend the current partition until all characters inside it have their last occurrence within the partition, then cut the partition as soon as it becomes safe.**

---

## 🧠 Algorithm

1. Create a dictionary `last`.
2. Traverse the string and store the last index of every character.
3. Initialize:

   ```python
   result = []
   start = 0
   end = 0
   ```

4. Traverse the string again.
5. For every character:
   - Update `end` using its last occurrence:

     ```python
     end = max(end, last[s[i]])
     ```

6. If `i == end`:
   - The current partition is complete.
   - Add its size:

     ```python
     result.append(end - start + 1)
     ```

   - Move `start` to the next position:

     ```python
     start = i + 1
     ```

7. Return `result`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The first traversal stores the last occurrence of every character: **O(n)**.
- The second traversal determines the partitions: **O(n)**.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(k)**

We use a dictionary to store the last occurrence of each character.

If `k` is the number of unique characters:

**Space Complexity = O(k)**

For the English lowercase alphabet, `k` is at most `26`, so this can effectively be considered **O(1)**.

---

## 📚 Concepts Used

- Greedy Algorithm
- Hash Map / Dictionary
- String Traversal
- Last Occurrence
- Range Expansion

---

## 🎯 Key Learning

- A **Hash Map** can be used to quickly find the last occurrence of each character.
- The `end` variable represents the farthest position the current partition must reach.
- We continuously expand `end` using:

  ```python
  end = max(end, last[s[i]])
  ```

- We can only finish a partition when:

  ```python
  i == end
  ```

- The greedy strategy is to **make a partition as soon as it is safe**, which maximizes the number of partitions.
- This problem is a great example of **Greedy + Hash Map** with **O(n) time**.
