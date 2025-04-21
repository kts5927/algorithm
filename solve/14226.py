from collections import deque

def cal(S):

    visited = [[False for _ in range(1001)] for _ in range(1001)]
    que = deque()
    que.append([1,0,0])
    time = 0
    while que:
        time += 1
        imo,clip,time = que.popleft()
        if imo+clip == S or imo-1 == S:
            return time+1
        if not visited[imo][imo]:
            que.append([imo,imo,time+1])
            visited[imo][clip] = True
        if imo+clip < 1001 and not visited[imo+clip][clip]:
            que.append([imo+clip,clip,time+1])
            visited[imo+clip][clip] = True
        if imo > 1 and not visited[imo-1][clip]:
            que.append([imo-1,clip,time+1])
            visited[imo-1][clip] = True
        
    
def sol():
    S = int(input())

    
    print(cal(S))
sol()