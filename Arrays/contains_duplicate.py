"""
Problem: Contains Duplicate (LeetCode #217)
Return True if any value appears at least twice.

Approach: HashSet - if element already in set, duplicate found
Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# ---- Test ----
print(contains_duplicate([1, 2, 3, 1]))     # True
print(contains_duplicate([1, 2, 3, 4]))     # False