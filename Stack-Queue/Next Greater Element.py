# ------------------------------------------------------------------
# 4. Next Greater Element
# ------------------------------------------------------------------
"""
Problem:
Given an array, for every element find the first greater element that
appears to its right. If no such element exists, output -1.
 
Companies: Amazon, Google, Zoho, Morgan Stanley
 
Approach:
- Traverse the array from right to left using a monotonic decreasing stack.
- For each element, pop all elements from the stack smaller than or equal
  to the current element (they can never be a "next greater" for anything
  further left).
- The top of the stack (if any) after popping is the next greater element.
- Push the current element onto the stack before moving left.
 
Time Complexity: O(n)  -- each element is pushed and popped at most once
Space Complexity: O(n)
"""
 
def next_greater_element(nums: list) -> list:
    n = len(nums)
    result = [-1] * n
    stack = []  # monotonic decreasing stack of values
 
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
 
    return result
 

# ---- Test ----
print(next_greater_element([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]
print(next_greater_element([3, 2, 1]))      # Output: [-1, -1, -1]