N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * (N * 3) for _ in range(2)]


def recur(j, i, cnt):
    global ans

    if N % 2:  
        if i == N:
            j += 1
            i = 0
        elif i == N + 1:
            j += 1
            i = 1
    else:  
        if i == N:
            j += 1
            i = 1
        elif i == N + 1:
            j += 1
            i = 0

    if j == N:
        if ans < cnt:
            ans = cnt
        return
    if arr[j][i] == 1 and not visited[0][j + i] and not visited[1][j - i]:
        visited[0][j + i] = True
        visited[1][j - i] = True
        recur(j, i + 2, cnt + 1)
        visited[0][j + i] = False
        visited[1][j - i] = False

    recur(j, i + 2, cnt)


ans = 0
recur(0, 0, 0)
Bcnt = ans 
ans = 0
recur(0, 1, 0)
Wcnt = ans  

print(Bcnt + Wcnt)