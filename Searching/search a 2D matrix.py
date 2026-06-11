# ─────────────────────────────────────────────
# 4. Search a 2D Matrix (LeetCode #74)
# Matrix: each row sorted, first element of row > last of prev row.
# Return True if target exists.
#
# Approach: Treat the matrix as a flat sorted array, apply binary search
# Time : O(log(m * n))
# Space: O(1)
# ─────────────────────────────────────────────
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
 
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]   # convert flat index → 2D
 
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
 
    return False
 
 
# ---- Test ----
print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))   # True
print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False