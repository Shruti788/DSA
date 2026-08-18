## 🔗 Problem

Given a list of non-negative integers `nums`, arrange them such that they form the **largest number** possible.

Return the largest number as a string.

---

## 📝 Example

### Example 1

**Input**

```text
nums = [10,2]
```

**Output**

```text
"210"
```

We can arrange the numbers as:

```text
2 + 10 = 210
```

which is larger than:

```text
10 + 2 = 102
```

Therefore, the answer is:

```text
"210"
```

---

### Example 2

**Input**

```text
nums = [3,30,34,5,9]
```

**Output**

```text
"9534330"
```

The correct order is:

```text
9, 5, 34, 3, 30
```

So:

```text
9534330
```

is the largest possible number.

---

## 💡 Approach

### Custom Sorting

The main idea is to **convert every number into a string** and then decide the correct order using a custom comparison.

First:

```python
nums = list(map(str, nums))
```

For every two strings `a` and `b`, compare:

```text
a + b
```

with:

```text
b + a
```

Whichever combination produces the larger number should come first.

For example:

```text
a = "3"
b = "30"
```

Compare:

```text
a + b = "330"
b + a = "303"
```

Since:

```text
"330" > "303"
```

`3` should come before `30`.

---

## 🧠 Why Compare `a + b` and `b + a`?

This is the key idea of the problem.

We are not simply sorting the numbers based on their individual values.

Instead, we want to know:

> **If I put `a` before `b`, do I get a larger number than putting `b` before `a`?**

For example:

```text
a = "9"
b = "34"
```

Compare:

```text
"9" + "34" = "934"
```

and:

```text
"34" + "9" = "349"
```

Since:

```text
934 > 349
```

`9` should come before `34`.

---

## 🔍 Example Walkthrough

For:

```text
nums = [3,30,34,5,9]
```

After converting the numbers to strings:

```text
["3", "30", "34", "5", "9"]
```

Now we compare pairs using:

```python
a + b
```

and:

```python
b + a
```

### Compare `"3"` and `"30"`

```text
"3" + "30" = "330"
"30" + "3" = "303"
```

Since:

```text
330 > 303
```

`"3"` should come before `"30"`.

---

### Compare `"34"` and `"3"`

```text
"34" + "3" = "343"
"3" + "34" = "334"
```

Since:

```text
343 > 334
```

`"34"` should come before `"3"`.

---

### Compare `"9"` and `"5"`

```text
"9" + "5" = "95"
"5" + "9" = "59"
```

Since:

```text
95 > 59
```

`"9"` should come before `"5"`.

---

After applying this comparison throughout the list, we get:

```text
["9", "5", "34", "3", "30"]
```

Finally, join them:

```python
result = ''.join(nums)
```

which gives:

```text
"9534330"
```

---

## 🛠️ How `compare()` Works

Our comparison function is:

```python
def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0
```

### If `a + b` is larger

```python
return -1
```

This tells Python:

```text
a should come before b
```

### If `b + a` is larger

```python
return 1
```

This tells Python:

```text
b should come before a
```

### If both are equal

```python
return 0
```

Their order does not matter.

---

## 🔑 Why Use `cmp_to_key`?

Python's `sort()` normally expects a **key function**.

But here, we need to compare **two elements at a time**:

```text
a and b
```

That's why we use:

```python
from functools import cmp_to_key
```

Then:

```python
nums.sort(key=cmp_to_key(compare))
```

`cmp_to_key()` allows our custom comparison function to work with Python's sorting algorithm.

So instead of sorting based on:

```text
value of a
```

we sort based on:

```text
a + b  vs  b + a
```

---

## ⚠️ Handling the All-Zero Case

Consider:

```text
nums = [0,0,0]
```

After sorting:

```text
["0", "0", "0"]
```

Joining them gives:

```text
"000"
```

But the expected answer is:

```text
"0"
```

Therefore, we check:

```python
if result[0] == '0':
    return '0'
```

If the first character is `0`, all numbers must be zero, so we simply return:

```text
"0"
```

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n log n × k)**

We sort `n` elements, which takes approximately:

```text
O(n log n)
```

But each comparison involves concatenating strings, which can take time proportional to the number of digits.

Therefore, more precisely:

**Time Complexity = O(n log n × k)**

where `k` is the maximum number of digits in a number.

---

### Space Complexity: **O(n)**

We convert all integers into strings and use Python's sorting mechanism.

Therefore:

**Space Complexity = O(n)**

---

## 📚 Concepts Used

- Custom Sorting
- String Manipulation
- `cmp_to_key`
- Comparator Function
- Greedy Ordering
- Array Traversal

---

## 🎯 Key Learning

The most important idea in this problem is:

> **Don't compare numbers individually. Compare the two possible combinations.**

For two numbers `a` and `b`:

```text
a + b
```

vs.

```text
b + a
```

Whichever produces the larger result should come first.

For example:

```text
"34" + "3" = "343"
"3" + "34" = "334"
```

Since:

```text
343 > 334
```

we place:

```text
34 before 3
```

This custom comparison allows us to arrange the numbers so that their concatenation forms the **largest possible number**.
