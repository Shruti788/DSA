# 1. Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

## Approach 1: Brute Force

- Compare every possible pair using nested loops.
- Time Complexity: O(n²)
- Space Complexity: O(1)

## Approach 2: Hash Map

- Store previously seen numbers and their indices in a dictionary.
- For each number, calculate the complement (`target - current_number`).
- If the complement already exists in the dictionary, return the indices.
- Otherwise, store the current number and continue.

- Time Complexity: O(n)
- Space Complexity: O(n)
