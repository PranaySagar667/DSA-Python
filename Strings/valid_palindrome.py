"""
Problem: Valid Palindrome (LeetCode #125)
A phrase is a palindrome if, after converting to lowercase and
removing non-alphanumeric characters, it reads the same forward and backward.

Approach: Two pointers from both ends, skip non-alphanumeric
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome(s):
    left , right = 0 , len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# ---- Test ----
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome(" "))                               # True