from collections import deque

# --- STACK (Last-In, First-Out / LIFO) ---
# In Python, a standard list is the most efficient way to implement a stack.
print("--- Stack Operations (using list) ---")
stack = [10, 20, 30]
print(f"Initial stack: {stack}")

# Push: Add to the end
stack.append(40)
print(f"After append(40): {stack}")

# Pop: Remove from the end
popped_val = stack.pop()
print(f"After pop(): {stack} (Popped value: {popped_val})")
print("-" * 30)
# --- TIME COMPLEXITY (Big O Notation) ---
# Stack (List):
# .append(val) -> O(1) amortized
# .pop()        -> O(1)
# Accessing top (stack[-1]) -> O(1)

# Queue (deque):
# .append(val)     -> O(1)
# .popleft()       -> O(1)
# .appendleft(val) -> O(1)
# .pop()           -> O(1)

print("-" * 30)


# --- QUEUE (First-In, First-Out / FIFO) ---
# For a queue, use collections.deque for O(1) additions and removals from both ends.
print("--- Queue Operations (using collections.deque) ---")
queue = deque([1, 2, 3])
print(f"Initial queue: {list(queue)}")

# Enqueue: Add to the tail (right side)
queue.append(4)
print(f"After append(4): {list(queue)}")

# Dequeue: Remove from the head (left side)
left_popped = queue.popleft()
print(f"After popleft(): {list(queue)} (Popped from left: {left_popped})")

# Add to the head (left side)
queue.appendleft(0)
print(f"After appendleft(0): {list(queue)}")

# Remove from the tail (right side)
right_popped = queue.pop()
print(f"After pop(): {list(queue)} (Popped from right: {right_popped})")
