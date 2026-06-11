# ─────────────────────────────────────────────
# 3. Find First and Last Position of Element (LeetCode #34)
# Return [first_index, last_index] of target in sorted array.
# Return [-1, -1] if not found.
#
# Approach: Two binary searches — one biased left, one biased right
# Time : O(log n)
# Space: O(1)
# ─────────────────────────────────────────────
def search_range(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
 
        while left <= right:
            mid = (left + right) // 2
 
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1   # keep searching left
                else:
                    left = mid + 1    # keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
 
        return bound
 
    return [find_bound(True), find_bound(False)]
 
 
# ---- Test ----
print(search_range([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]