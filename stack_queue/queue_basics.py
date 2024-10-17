# Adding to a queue = enqueue
# Deleting from a queue = dequeue

# Sophisticated implementation needed as:
# Dynamic array = O(n)
# Linked List = O(1)

# Data structure called deque (deck) -> Allows entry + deletion from both sides

import collections

queue = collections.deque([1, 2, 3])

# Enqueueing elements (Adding)
queue.append(4)
queue.append(5)

print("Queue after appending elements\n" + str(queue))

# Dequeueing elements (Removing)
queue.popleft() # 1
queue.popleft() # 2

print("Queue after popping elements\n" + str(queue))

queue[0] # Check the element at the front of the queue

# Get size
len(queue) # 3

