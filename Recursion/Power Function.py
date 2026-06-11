# ─────────────────────────────────────────────
# 2. Power Function — Pow(x, n) (LeetCode #50)
# Implement x raised to the power n (x^n).
#
# Approach: Fast exponentiation — halve the exponent each call
#           x^n = (x^(n/2))^2   → reduces O(n) multiplications to O(log n)
#           Handle negative n: x^-n = 1 / x^n
# Time : O(log n)
# Space: O(log n)  — call stack depth
# ─────────────────────────────────────────────
def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
 
    half = my_pow(x, n // 2)
 
    if n % 2 == 0:
        return half * half          # even power
    else:
        return half * half * x      # odd power — one extra x
 
 
# ---- Test ----
print(my_pow(2.0, 10))    # 1024.0
print(my_pow(2.0, -2))    # 0.25
print(my_pow(3.0, 4))     # 81.0