import sys
sys.setrecursionlimit(10**7)

def check(i):
    for j in range(len(lists[i])):
        global answer
        if not visit[lists[i][j]]:
            visit[lists[i][j]] = True
            if color[i] == 0:
                color[lists[i][j]] = 1
            else : 
                color[lists[i][j]] = 0
            
            check(lists[i][j])
        elif color[i] == color[lists[i][j]]:
            answer = False
            break
            


K = int(sys.stdin.readline())
for i in range(K):
    V,E = map(int,sys.stdin.readline().split())
    lists = [[] for j in range(V+1)]
    color = [0 for j in range(V+1)]
    visit = [False for j in range(V+1)]
    answer = True
    for j in range(E):
        u,v = map(int,sys.stdin.readline().split())
        lists[u] += [v]
        lists[v] += [u]
    for i in range(1,len(lists)):
        check(i)
    if answer == True:
        print('YES')
    else : print('NO')

