# ─────────────────────────────────────────────
# 1. Climbing Stairs (LeetCode #70)
# n stairs, climb 1 or 2 steps at a time. How many distinct ways?
#
# Approach: Recursive with memoization (top-down DP)
#           ways(n) = ways(n-1) + ways(n-2)  → Fibonacci pattern
# Time : O(n)
# Space: O(n)  — memo dict + call stack
# ─────────────────────────────────────────────
def climb_stairs(n, memo={}):
    if n <= 2:
        return n
 
    if n in memo:
        return memo[n]
 
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]
 
 
# ---- Test ----
print(climb_stairs(2))   # 2
print(climb_stairs(5))   # 8
print(climb_stairs(10))  # 89