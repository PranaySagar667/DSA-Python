"""
Problem: Valid Anagram (LeetCode #242)
Given two strings s and t, return True if t is an anagram of s.

Approach: Count character frequencies using a dictionary
Time Complexity: O(n)
Space Complexity: O(1) — at most 26 keys
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True

# ---- Test ----
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False