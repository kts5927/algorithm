import time
import random
from collections import deque

start_time = time.time()
lst = []
que = deque()
for _ in range(500000):
    # lst.append(random.randrange(1,100000))
    que.append(random.randrange(1,5000))
    que.popleft()
end_time = time.time()

print("50만번 append 수행 시간:", end_time - start_time, "초")