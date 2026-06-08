"""
Problem: Two Sum (LeetCode #1)
Given an array of integers and a target, return indices of two numbers that add up to target.

Approach: HashMap - store complement as we iterate
Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums,target):
    seen = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement] , i]
        seen[num] = i
    return []

    
print(two_sum([2,7,3,4,2],11))      #[1, 3]
print(two_sum([3, 2, 4], 6))        # [1, 2]

















