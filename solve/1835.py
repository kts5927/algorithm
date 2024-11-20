from collections import deque
N = int(input())
card = deque()
for i in range(1,N+1):
    if len(card) > 0:
        for j in range(N-i+2,0,-1):
            card.appendleft(card.pop())
    card.appendleft(N-i+1)

card.appendleft(card.pop())

print(*card)