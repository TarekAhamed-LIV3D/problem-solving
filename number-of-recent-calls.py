from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)

obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))