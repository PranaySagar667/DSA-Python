# ─────────────────────────────────────────────
# 4. Kth Largest Element in an Array (LeetCode #215)
# Find the kth largest element (not kth distinct).
#
# Approach: QuickSelect — partition like QuickSort but only recurse
#           into the side that contains kth position
#           Average O(n), worst O(n²); no need to sort the full array
# Time : O(n) average, O(n²) worst
# Space: O(1)
# ─────────────────────────────────────────────
def find_kth_largest(nums, k):
    target = len(nums) - k      # kth largest = (n-k)th smallest index

    def quickselect(left, right):
        pivot = nums[right]
        p = left                # partition pointer

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]   # place pivot

        if p == target:
            return nums[p]
        elif p < target:
            return quickselect(p + 1, right)
        else:
            return quickselect(left, p - 1)

    return quickselect(0, len(nums) - 1)


# ---- Test ----
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))        # 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
