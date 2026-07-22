# Longest Valid Parentheses

A Python solution to the **Longest Valid Parentheses** problem using the **Stack** data structure. The program finds the length of the longest valid (well-formed) parentheses substring in **O(n)** time complexity.

## 📌 Problem Statement

Given a string containing only `'('` and `')'`, return the length of the **longest valid (well-formed) parentheses substring**.

### Example

| Input | Output |
|-------|--------|
| `"(()"` | `2` |
| `")()())"` | `4` |
| `""` | `0` |

---

## 🚀 Approach

This solution uses a **Stack** to store the indices of parentheses.

- Initialize the stack with `-1` as a base index.
- Push the index whenever `'('` is encountered.
- Pop the stack when `')'` is encountered.
- If the stack becomes empty, push the current index as the new base.
- Otherwise, calculate the current valid substring length using:
  ```python
  current_length = current_index - stack[-1]
  ```
- Update the maximum length whenever a longer valid substring is found.

---

## 💡 Algorithm

1. Create a stack initialized with `[-1]`.
2. Traverse the string character by character.
3. If the character is `'('`, push its index.
4. If the character is `')'`:
   - Pop the top element.
   - If the stack becomes empty, push the current index.
   - Otherwise, calculate the valid substring length and update the answer.
5. Return the maximum length.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## 🛠️ Technologies Used

- Python 3
- Stack Data Structure

---

## 📂 Project Structure

```
Longest-Valid-Parentheses/
│── longest_valid_parentheses.py
│── README.md
```

---

## ▶️ Sample Output

```
Input: "(()"
Output: 2

Input: ")()())"
Output: 4

Input: ""
Output: 0
```

---

## 🎯 Key Concepts

- Stack
- String Processing
- Index Tracking
- Linear Time Algorithm
- Parentheses Matching

---

## 📖 Learning Outcome

This project demonstrates how a **Stack** can efficiently solve parentheses matching problems by tracking indices and calculating valid substring lengths in a single traversal.

---

### ⭐ If you found this project useful, consider giving it a Star!
