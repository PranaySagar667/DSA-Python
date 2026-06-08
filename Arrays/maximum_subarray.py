"""
Problem: Maximum Subarray (LeetCode #53)
Find the contiguous subarray with the largest sum.

Approach: Kadane's Algorithm - extend or restart subarray
Time Complexity: O(n)
Space Complexity: O(1)
"""
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num , current_sum + num)
        max_sum = max(current_sum , max_sum)
    return max_sum

# ---- Test ----
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1]))                              # 1
print(max_subarray([5, 4, -1, 7, 8]))                 # 23