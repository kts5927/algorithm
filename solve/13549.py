from collections import deque

N , M = map(int,input().split())

if N >= M:
    print(N-M)
else:
    que = deque()
    que.append([N,0])
    visited = [0]*100001
    ans = 1000000
    while que:
        q , method = que.popleft()
        
        if q == M and ans > method:
            ans = method
            continue
            
        for i in q+1,q-1:
            if 0 <= i <= 100000:
                if visited[i] == 0:
                    visited[i] = visited[q]+1
                    que.append([i,method+1])
                elif visited[i]  == visited[q]+1:
                    que.append([i,method+1])
                    

        if 0 <= q <= 50000:
            if visited[q*2] == 0:
                visited[q*2] = visited[q]+1
                que.append([q*2,method])
            elif visited[q*2]  == visited[q]+1:
                que.append([q*2,method])

    print(ans)