import sys
sys.setrecursionlimit(10**5)

def DFS(a):
    global n
    
    while True:
        if n < N-1 and isCorrect[n+1] in tree[a]:
            n+=1
            DFS(isCorrect[n])
        else:
            return



N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    A,B = map(int,sys.stdin.readline().split())
    
    tree[A].append(B)
    tree[B].append(A)

check = [False for _ in range(N+1)]
ans = 0
isCorrect = list(map(int,sys.stdin.readline().split()))
n = 0
if isCorrect[0] == 1:
    DFS(1)
else:
    ans = 1

if n == N-1:
    print(1)
else:
    print(0)