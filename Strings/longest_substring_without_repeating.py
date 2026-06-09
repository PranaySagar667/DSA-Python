"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Find the length of the longest substring without repeating characters.

Approach: Sliding window — expand right, shrink left on duplicate
Time Complexity: O(n)
Space Complexity: O(n)
"""

def length_of_longest_substring(s):
    seen = {}       # char -> last seen index
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1     # shrink window past duplicate
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# ---- Test ----
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")