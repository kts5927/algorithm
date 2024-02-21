from collections import deque
N , M = map(int,input().split())

singer = [[] for _ in range(N+1)]
count = [0 for _ in range(N+1)]
for _ in range(M):
    a = list(map(int,input().split()))
    for i in range(1,len(a)-1):
        singer[a[i]].append(a[i+1])
        count[a[i+1]] += 1

visited = [False for _ in range(N+1)]

cal = deque() 
for i in range(1,len(count)):
    if count[i] == 0 :
        cal.append(i)

ans = []        
while cal:
    a = cal.popleft()
    visited[a] = True
    
    ans.append(a)
    
    for i in singer[a]:
        count[i] -= 1
        if count[i] == 0:
            cal.append(i)

if len(ans) != N :
    print(0)
else : 
    for i in ans:
        print(i)
