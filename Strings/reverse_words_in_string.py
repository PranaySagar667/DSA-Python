"""
Problem: Reverse Words in a String (LeetCode #151)
Given a string, reverse the order of words.
Words are separated by spaces. Remove extra spaces.

Approach: Split on whitespace (handles multiple spaces), reverse list, rejoin
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_words(s):
    words = s.split()       # split() handles multiple/leading/trailing spaces
    return " ".join(reversed(words))

# ---- Test ----
print(reverse_words("the sky is blue"))       # "blue is sky the"
print(reverse_words("  hello world  "))       # "world hello"
print(reverse_words("a good   example"))      # "example good a" 