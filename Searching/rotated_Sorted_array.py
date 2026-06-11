# 2. Search in Rotated Sorted Array (LeetCode #33)
# Array was rotated at some pivot. Find target index or -1.
#
# Approach: Modified binary search — identify which half is sorted,
#           then check if target lies in that half
# Time : O(log n)
# Space: O(1)
# ─────────────────────────────────────────────
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
 
    while left <= right:
        mid = (left + right) // 2
 
        if nums[mid] == target:
            return mid
 
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
 
    return -1
 
 
# ---- Test ----
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # -1