from collections import deque

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
chain = deque(lst)
count = 0


while len(chain) > 2:
    a = chain.popleft()
    b = chain.pop()
    c = chain.pop()
    
    a -= 1
    b += c + 1
    if a > 0:
        chain.appendleft(a)
    chain.append(b)
    count += 1


if len(chain) == 2:
    count += 1    
print(count)