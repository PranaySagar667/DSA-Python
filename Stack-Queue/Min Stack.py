# ------------------------------------------------------------------
# 2. Min Stack (Design a stack with O(1) getMin)
# ------------------------------------------------------------------
"""
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time O(1).
 
Companies: Amazon, Microsoft, Bloomberg
 
Approach:
- Maintain a secondary stack (min_stack) that tracks the minimum value
  seen so far at each level of the main stack.
- Push to min_stack whenever the new value is <= current min.
- Pop from min_stack whenever the popped value equals the current min.
 
Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""
 
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
 
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
 
    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
 
    def top(self) -> int:
        return self.stack[-1]
 
    def get_min(self) -> int:
        return self.min_stack[-1]
 

min_stack = MinStack()  
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2