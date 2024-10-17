from collections import deque

class Example:
    def __init__(self):
        
        self.queue = deque()

    # Store t in a queue until you realize that is more than 3000 time units old
    def recent_calls(self, t:int) -> int:

        while self.queue and self.queue[0] < 3000 - t:
            self.queue.popleft()

        self.queue.append(t)
        return(len(self.queue))
