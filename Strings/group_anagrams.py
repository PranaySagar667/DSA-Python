"""
Problem: Group Anagrams (LeetCode #49)
Given a list of strings, group the anagrams together.

Approach: Use sorted word as key in a hashmap — anagrams share the same sorted form
Time Complexity: O(n * k log k) where k = max word length
Space Complexity: O(n * k)
"""

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))   # "eat","tea","ate" all sort to ('a','e','t')
        groups[key].append(word)
    return list(groups.values())

# ---- Test ----
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]
print(group_anagrams([""]))   # [['']]
print(group_anagrams(["a"]))  # [['a']] 