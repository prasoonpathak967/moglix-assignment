def longest_valid_parentheses(s: str) -> int:
    # Stack stores indices; start with -1 as a base for length calculation
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:
                # No matching '(' left, push current index as new base
                stack.append(i)
            else:
                # Valid substring found, update max length
                max_length = max(max_length, i - stack[-1])

    return max_length


# --- Test cases ---
if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))     # Output: 2
    print(longest_valid_parentheses(")()())"))  # Output: 4
    print(longest_valid_parentheses(""))        # Output: 0