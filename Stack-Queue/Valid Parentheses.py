# ------------------------------------------------------------------
# 1. Valid Parentheses
# ------------------------------------------------------------------
"""
Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
A string is valid if brackets are closed in the correct order and every
opening bracket has a matching closing bracket.
 
Companies: Amazon, Google, Microsoft, Facebook
 
Approach:
- Use a stack. Push opening brackets.
- On a closing bracket, pop and check it matches the corresponding opener.
- String is valid only if stack is empty at the end.
 
Time Complexity: O(n)
Space Complexity: O(n)
"""
 
def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
 
    for char in s:
        if char in pairs.values():          # opening bracket
            stack.append(char)
        elif char in pairs:                 # closing bracket
            if not stack or stack.pop() != pairs[char]:
                return False
        # ignore any non-bracket characters if present
 
    return not stack

# ---- Test ----
print(is_valid_parentheses("()"))           # True
print(is_valid_parentheses("()[]{}"))       # True
print(is_valid_parentheses("(]"))           # False