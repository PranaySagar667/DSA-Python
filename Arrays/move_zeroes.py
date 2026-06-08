"""
Problem: Move Zeroes (LeetCode #283)
Move all 0s to end while maintaining relative order of non-zero elements.

Approach: Two pointers - left pointer places non-zeros, right scans
Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeroes(nums):
    left = 0 
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

# ---- Test ----
print(move_zeroes([0, 1, 0, 3, 12, 19, 0]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))         # [1, 0, 0]