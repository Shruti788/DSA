# 🔗 Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on the `i`-th day.

You can buy and sell the stock multiple times, but you can hold **at most one stock at a time**.

Return the **maximum profit** you can achieve.

---

## 📝 Example

### Example 1

**Input**

```text
prices = [7,1,5,3,6,4]
```

**Output**

```text
7
```

**Explanation**

- Buy at `1` and sell at `5` → profit = `4`
- Buy at `3` and sell at `6` → profit = `3`

Total profit:

```text
4 + 3 = 7
```

---

## 💡 Approach

### Greedy

We compare each day's price with the previous day's price.

If today's price is greater than yesterday's price, we take that profit:

```python
if prices[i] > prices[i - 1]:
    profit += prices[i] - prices[i - 1]
```

The greedy idea is:

> **Whenever the price increases from one day to the next, capture that increase.**

We don't need to explicitly decide where to buy and sell.

For example:

```text
prices = [1,2,3,4,5]
```

Instead of thinking:

```text
Buy at 1 → Sell at 5
```

we can think:

```text
1 → 2 = +1
2 → 3 = +1
3 → 4 = +1
4 → 5 = +1
```

Both approaches give the same total profit:

```text
4
```

Similarly, when the price decreases, we simply ignore that difference because it would not contribute to profit.

---

## 🧠 Algorithm

1. Initialize `profit = 0`.
2. Start traversing from index `1`.
3. Compare `prices[i]` with `prices[i - 1]`.
4. If:

   ```python
   prices[i] > prices[i - 1]
   ```

   add the difference to `profit`.

5. If the price decreases or stays the same, do nothing.
6. Return `profit`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- We traverse the `prices` array once.
- Each price is compared with the previous price exactly once.

Therefore,

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

We only use one additional variable:

```python
profit
```

No additional data structures are required.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Greedy Algorithm
- Array Traversal
- Stock Trading
- Local Profit Calculation

---

## 🎯 Key Learning

- We don't need to find the exact buy and sell days explicitly.
- Every **positive price difference** contributes to the maximum possible profit.
- When the price increases, we add the difference to `profit`.
- When the price decreases or remains the same, we simply ignore it.
- A sequence of consecutive increases can be treated as multiple small profits, which gives the same result as buying at the beginning and selling at the end.
- This is a classic example of a **Greedy Algorithm** with **O(n) time and O(1) space**.
