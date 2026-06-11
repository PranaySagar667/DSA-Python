# ─────────────────────────────────────────────
# 3. Subsets (LeetCode #78)
# Return all possible subsets (power set) of a list of unique integers.
#
# Approach: Backtracking — at each index, choose to include or skip element
#           Build subsets by branching: include nums[i] → recurse → backtrack
# Time : O(2^n * n)  — 2^n subsets, each up to n elements
# Space: O(2^n * n)
# ─────────────────────────────────────────────
def subsets(nums):
    result = []
 
    def backtrack(start, current):
        result.append(list(current))    # snapshot of current subset
 
        for i in range(start, len(nums)):
            current.append(nums[i])     # include nums[i]
            backtrack(i + 1, current)   # recurse on remaining
            current.pop()               # backtrack — remove nums[i]
 
    backtrack(0, [])
    return result
 
 
# ---- Test ----
print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]