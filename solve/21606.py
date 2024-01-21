import sys

def check(i) :
    visited[i] = True
    for j in range(len(lists[i])):
        global count
        if not visited[lists[i][j]]:
            if A[lists[i][j]] == 0 :
                check(lists[i][j])
            
            elif A[lists[i][j]] == 1:
                count+=1
            

N = int(sys.stdin.readline())
A = []
a = int(input())
for i in range(N):
    A.append(a%10)
    a = a//10
count = 0
A.append(0)
A.reverse()
lists = [[] for j in range(N+1)]
for j in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    lists[u] += [v]
    lists[v] += [u]
    
for i in range(len(lists)):
    visited = [False for j in range(N+1)]
    if A[i] == 1:
        check(i)
    
print(count)