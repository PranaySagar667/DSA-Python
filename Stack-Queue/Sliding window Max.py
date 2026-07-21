# ------------------------------------------------------------------
# 5. Sliding Window Maximum
# ------------------------------------------------------------------
"""
Problem:
Given an array `nums` and a sliding window of size `k` moving from left
to right, return the maximum element in each window.
 
Companies: Amazon, Google, Facebook, Bloomberg (very frequently asked)
 
Approach:
- Use a deque (double-ended queue) to store INDICES of useful elements.
- The deque is maintained in decreasing order of values (front = max of
  current window).
- Before adding a new index, remove indices from the back whose values
  are smaller than the current element (they'll never be the max again).
- Remove the front index if it has slid out of the current window.
- The front of the deque is always the max of the current window.
 
Time Complexity: O(n)  -- each index is added/removed from deque at most once
Space Complexity: O(k)
"""
 
from collections import deque
 
def sliding_window_maximum(nums: list, k: int) -> list:
    if not nums or k <= 0:
        return []
 
    dq = deque()   # stores indices, values in decreasing order
    result = []
 
    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        if dq and dq[0] <= i - k:
            dq.popleft()
 
        # Remove indices whose values are smaller than current num
        while dq and nums[dq[-1]] < num:
            dq.pop()
 
        dq.append(i)
 
        # Start recording results once the first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
 
    return result

# ---- Test ----
nums = [1, 3, -1, -3, 5, 3, 6, 7] 
k = 3
print(sliding_window_maximum(nums, k))  # Output: [3, 3, 5, 5, 6, 7]