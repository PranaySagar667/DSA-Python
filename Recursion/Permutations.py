# ─────────────────────────────────────────────
# 4. Permutations (LeetCode #46)
# Return all permutations of a list of distinct integers.
#
# Approach: Backtracking — swap current position with each remaining element,
#           recurse for next position, then swap back (backtrack)
# Time : O(n! * n)  — n! permutations, each of length n
# Space: O(n)       — call stack depth (excluding output)
# ─────────────────────────────────────────────
def permutations(nums):
    result = []
 
    def backtrack(start):
        if start == len(nums):
            result.append(list(nums))   # full permutation reached
            return
 
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]   # swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]   # un-swap (backtrack)
 
    backtrack(0)
    return result
 
 
# ---- Test ----
print(permutations([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]