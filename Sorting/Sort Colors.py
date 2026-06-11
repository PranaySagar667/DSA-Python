# ─────────────────────────────────────────────
# 2. Sort Colors — Dutch National Flag (LeetCode #75)
# Sort array with values 0, 1, 2 in-place without sort().
#
# Approach: Three-pointer partition (low, mid, high)
#           0s go left, 2s go right, 1s stay in middle
# Time : O(n)
# Space: O(1)
# ─────────────────────────────────────────────
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1           # don't increment mid — swapped element unchecked

    return nums


# ---- Test ----
print(sort_colors([2, 0, 2, 1, 1, 0]))   # [0, 0, 1, 1, 2, 2]
print(sort_colors([2, 0, 1]))             # [0, 1, 2]