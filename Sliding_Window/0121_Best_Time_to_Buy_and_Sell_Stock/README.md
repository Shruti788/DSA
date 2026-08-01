## 🔗 Problem

You are given an array `prices` where `prices[i]` is the price of a stock on the `i`th day.

You want to maximize your profit by choosing:

- One day to buy the stock.
- A different future day to sell the stock.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

---

## 📝 Example

### Example 1

**Input**

```text
prices = [7,1,5,3,6,4]
```

**Output**

```text
5
```

**Explanation**

- Buy on day 2 at price `1`.
- Sell on day 5 at price `6`.

Profit = `6 - 1 = 5`

---

### Example 2

**Input**

```text
prices = [7,6,4,3,1]
```

**Output**

```text
0
```

**Explanation**

The prices keep decreasing, so no profit can be made.

---

## 💡 Approach

### Sliding Window

Maintain the minimum stock price seen so far while traversing the array.

- Initialize `min_price` as the first day's price.
- Iterate through each stock price.
- If the current price is lower than `min_price`, update `min_price`.
- Otherwise, calculate the profit by selling at the current price.
- Update the maximum profit whenever a larger profit is found.

This ensures that the buying day always comes before the selling day.

---

## 🧠 Algorithm

1. Initialize:
   - `min_price = prices[0]`
   - `max_profit = 0`
2. Traverse each price in the array.
3. If the current price is smaller than `min_price`, update `min_price`.
4. Otherwise:
   - Calculate `profit = price - min_price`.
   - Update `max_profit`.
5. Return `max_profit`.

---

## ⏱ Complexity Analysis

### Time Complexity: **O(n)**

- The array is traversed once.
- Each element is processed exactly once.

Therefore,

**Time Complexity = O(n)**

where:

- **n** = number of stock prices.

---

### Space Complexity: **O(1)**

- Only two variables (`min_price` and `max_profit`) are used.

Therefore,

**Space Complexity = O(1)**

---

## 📚 Concepts Used

- Sliding Window
- Greedy
- Array Traversal

---

## 🎯 Key Learning

- Instead of checking every pair of buying and selling days (**O(n²)**), keep track of the lowest price seen so far.
- At each step, calculate the profit if the stock is sold today.
- Updating the minimum buying price and the maximum profit in a single traversal gives an optimal **O(n)** solution.
