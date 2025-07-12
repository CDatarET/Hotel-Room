# Hotel-Room
CodeChef Difficulty 1169 Problem. 

# Maximum Number of People in the Room

## Problem Statement

There are initially `X` people in a room.

You are given an array `A` of length `N` which describes the following events:

- If `A[i] ≥ 0`, then `A[i]` people enter the room at the `i`-th minute.  
  For example, if `A[2] = 3`, then `3` people enter the room at the 2nd minute.
  
- If `A[i] < 0`, then `|A[i]|` people leave the room at the `i`-th minute.  
  Here `|A[i]|` denotes the absolute value of `A[i]`.  
  For example, if `A[4] = -2`, then `2` people leave the room at the 4th minute.

Determine the maximum number of people in the room at any moment of time.

It is guaranteed in the input that at any moment of time, the number of people in the room does not become negative.

---

## Input Format

- The first line will contain `T` — the number of test cases. Then the test cases follow.
- The first line of each test case consists of two integers `N` and `X` — the length of the array `A` and the number of people in the room initially.
- The second line of each test case contains `N` integers `A[1], A[2], A[3], ..., A[N]`.

---

## Output Format

For each test case, output the maximum number of people in the room at any point of time.

---
