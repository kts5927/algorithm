from collections import deque

N , M = map(int,input().split())

target = [list(map(int,input().strip())) for _ in range(N)]
deq = deque()
for i in range(N):
    for j in range(M):
        if target[i][j] == 1:
            deq.append([i,j])
ans = 0
while deq:
    y,x = deq.popleft()
    hit = [0 for _ in range(10)]
    dup = False
    for i in range(max(0, y-9), min(N-1, y+9)+1):
        for j in range(max(0, x-9), min(M-1, x+9)+1):
            location = max(abs(y-i),abs(x-j))
            if location < 10:
                if target[i][j] == 1:
                    if hit[location] == 0 :
                        hit[location] = 1
                    elif hit[location] == 1 :
                        dup = True
                        break
        if dup:
            break
    if sum(hit) == 10 and not dup:
        ans = [x,y]
        break

if ans != 0:
    print(ans[1],ans[0])
else:
    print(-1)
    
