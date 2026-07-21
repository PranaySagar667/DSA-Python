# ------------------------------------------------------------------
# 3. Implement Queue using Two Stacks
# ------------------------------------------------------------------
"""
Problem:
Implement a First-In-First-Out (FIFO) queue using only two stacks.
The queue should support enqueue, dequeue, peek, and empty operations.
 
Companies: Amazon, Adobe, Flipkart
 
Approach:
- Use two stacks: `in_stack` for enqueue operations, `out_stack` for dequeue.
- On dequeue/peek, if `out_stack` is empty, pour all elements from
  `in_stack` into `out_stack` (this reverses the order to FIFO).
- Amortized cost stays O(1) per operation since each element is moved
  at most once between the two stacks.
 
Time Complexity: O(1) amortized per operation
Space Complexity: O(n)
"""
 
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
 
    def enqueue(self, x: int) -> None:
        self.in_stack.append(x)
 
    def dequeue(self) -> int:
        self._transfer_if_needed()
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()
 
    def peek(self) -> int:
        self._transfer_if_needed()
        if not self.out_stack:
            raise IndexError("peek from empty queue")
        return self.out_stack[-1]
 
    def is_empty(self) -> bool:
        return not self.in_stack and not self.out_stack
 
    def _transfer_if_needed(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
 

# ---- Test ----
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())     # Output: 2