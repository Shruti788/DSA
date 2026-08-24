# 🔗 Problem

At a lemonade stand, each lemonade costs **$5**.

Customers are standing in a queue and pay with either a `$5`, `$10`, or `$20` bill.

You must provide the correct change to each customer.

Initially, you have **no money**.

Return `True` if you can provide the correct change to every customer. Otherwise, return `False`.

---

## 📝 Example

### Example 1

**Input**

```text
bills = [5,5,5,10,20]
```

**Output**

```text
true
```

**Explanation**

- Customer 1 pays `$5` → no change needed.
- Customer 2 pays `$5` → no change needed.
- Customer 3 pays `$5` → no change needed.
- Customer 4 pays `$10` → give one `$5` as change.
- Customer 5 pays `$20` → give one `$10` and one `$5` as change.

Therefore, every customer can receive the correct change.

---

### Example 2

**Input**

```text
bills = [5,5,10,10,20]
```

**Output**

```text
false
```

**Explanation**

After serving the first four customers, there are no `$5` bills left.

The last customer pays `$20` and needs `$15` change, but we cannot provide it.

Therefore, the answer is `False`.

---

## 💡 Approach

### Greedy + Counting

We maintain two variables:

```python
five = 0
ten = 0
```

These represent the number of `$5` and `$10` bills currently available.

We process each customer one by one.

### When the customer pays `$5`

No change is required, so we simply increase the number of `$5` bills:

```python
five += 1
```

### When the customer pays `$10`

We need to give `$5` as change.

If we don't have a `$5`, we cannot serve the customer:

```python
if five == 0:
    return False
```

Otherwise:

```python
five -= 1
ten += 1
```

### When the customer pays `$20`

We need to give `$15` as change.

There are two possible combinations:

```text
$10 + $5
```

or

```text
$5 + $5 + $5
```

We prefer:

```python
if five > 0 and ten > 0:
    five -= 1
    ten -= 1
```

because keeping `$5` bills is more useful for future customers.

If `$10 + $5` is not possible, we try three `$5` bills:

```python
elif five >= 3:
    five -= 3
```

If neither combination is possible, we return `False`.

The greedy idea is:

> **When giving `$15` change, use a `$10` + `$5` combination first so that we preserve as many `$5` bills as possible.**

---

## 🧠 Algorithm

1. Initialize:
   - `five = 0`
   - `ten = 0`

2. Traverse every bill in `bills`.
3. If the bill is `$5`:
   - Increase `five`.

4. If the bill is `$10`:
   - Check whether a `$5` is available.
   - If not, return `False`.
   - Otherwise, give one `$5` as change.
   - Increase `ten`.

5. If the bill is `$20`:
   - First try to give `$10 + $5`.
   - If that is not possible, try to give three `$5` bills.
   - If neither is possible, return `False`.

6. After serving all customers successfully, return `True`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- We traverse the `bills` array once.
- Each customer is processed in constant time.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We only maintain two counters:

```python
five
ten
```

No additional data structures are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Array Traversal
- Counting
- Conditional Logic

---

## 🎯 Key Learning

- Greedy algorithms make the **best local decision** at every step.
- For a `$20` bill, always prefer giving **`$10 + $5`** instead of three `$5` bills.
- This preserves more `$5` bills, which are more important because they are required to give change for `$10` bills.
- We only need to keep track of `$5` and `$10` bills because `$20` bills are never useful for giving change.
- This problem is a great example of **Greedy + Counting** with **O(n) time and O(1) space**.
