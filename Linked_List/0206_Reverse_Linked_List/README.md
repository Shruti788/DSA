# 🔗 Problem

Given the head of a singly linked list, reverse the list and return the reversed list.

For example:

```text
1 → 2 → 3 → 4 → 5 → None
```

After reversing:

```text
5 → 4 → 3 → 2 → 1 → None
```

---

## 📝 Example

### Example 1

**Input:**

```text
head = [1,2,3,4,5]
```

**Output:**

```text
[5,4,3,2,1]
```

**Explanation:**

The original linked list is:

```text
1 → 2 → 3 → 4 → 5 → None
```

After reversing:

```text
5 → 4 → 3 → 2 → 1 → None
```

---

## 💡 Approach

We use **three pointers**:

- `prev` → keeps track of the previous node
- `curr` → points to the current node
- `next_node` → temporarily stores the next node

Initially:

```python
prev = None
curr = head
```

For every node:

1. Save the next node so we don't lose the rest of the list.
2. Reverse the current node's pointer.
3. Move `prev` to the current node.
4. Move `curr` to the saved next node.

The key operation is:

```python
curr.next = prev
```

This changes the direction of the link.

---

## 🧠 Algorithm

```text
Set prev = None
Set curr = head

While curr is not None:

    Save the next node
    next_node = curr.next

    Reverse the current node's pointer
    curr.next = prev

    Move prev forward
    prev = curr

    Move curr forward
    curr = next_node

Return prev
```

---

## ⏱ Complexity Analysis

### Time Complexity

```text
O(n)
```

Each node is visited exactly once.

### Space Complexity

```text
O(1)
```

Only a few pointers are used, regardless of the size of the linked list.

---

## 📚 Concepts Used

- Linked List
- Singly Linked List
- Pointers
- Iteration
- In-place Modification
- Pointer Reversal

---

## 🎯 Key Learning

The most important concept is **reversing a linked list using pointers**.

The crucial line is:

```python
curr.next = prev
```

It changes:

```text
curr → next
```

into:

```text
curr → prev
```

We must save `curr.next` **before** changing the pointer:

```python
next_node = curr.next
```

Otherwise, we would lose access to the remaining part of the linked list.

The overall pattern is:

```text
Save → Reverse → Move prev → Move curr
```

This iterative pointer-reversal technique is one of the most important fundamental patterns for Linked List problems.
