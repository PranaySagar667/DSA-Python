# ─────────────────────────────────────────────
# 5. Sqrt(x) — Integer Square Root (LeetCode #69)
# Return floor(sqrt(x)) without using built-in sqrt.
#
# Approach: Binary search on answer space [0, x]
#           If mid*mid <= x, candidate is mid — search right for larger
# Time : O(log x)
# Space: O(1)
# ─────────────────────────────────────────────
def my_sqrt(x):
    if x < 2:
        return x
 
    left, right = 1, x // 2
    result = 1
 
    while left <= right:
        mid = (left + right) // 2
 
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid        # best candidate so far
            left = mid + 1
        else:
            right = mid - 1
 
    return result
 
 
# ---- Test ----
print(my_sqrt(4))    # 2
print(my_sqrt(8))    # 2  (floor of 2.828...)
print(my_sqrt(25))   # 5