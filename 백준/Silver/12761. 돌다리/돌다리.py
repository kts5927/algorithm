from collections import deque
a, b, N, M = map(int,input().split())
v = [0 for _ in range(100001)]
def cal(l):   
    arr = [l+1,l-1,l*a,-l*a,l*b,-l*b,l+a,l-a,l+b,l-b]
    return arr

def bfs(s):
    que = deque()
    que.append(s)
    v[s]
    while que:
        n = que.popleft()
        next = cal(n)
        for i in next:
            if 0<=i<100001 and not v[i]:
                v[i] = v[n]+1
                que.append(i)
                if i == M:
                    return
bfs(N)
print(max(v))