from collections import deque


N = int(input())

lst = []
for i in range(1,N+1):
    lst.append(i)
    
cal = deque(lst)

ans = []
while cal:
    if cal:
        ans.append(cal.popleft())
    
    if cal:
        cal.append(cal.popleft())
        
print(*ans)