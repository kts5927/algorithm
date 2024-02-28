import sys
sys.setrecursionlimit(10**6)

def union(x , y , w):
    value[x] -= w
    parent[x] = y
    parentvalue[x] = value[y]
    
def findparent(x):
    if parent[x] != x:
        p,pv = parent[x],parentvalue[x]
        parent[x] = findparent(p)
        value[x] += value[p]-pv
        parentvalue[x] = value[parent[x]]
    return parent[x]

while 1:
    N , M = map(int,input().split())
    if N == 0 :
        break
    
    value = [0 for _ in range(N+1)]
    parentvalue = [0]*(N+1)
    parent = []
    for i in range(N+1):
        parent.append(i)
    for _ in range(M):
        Q = input().split()
        if Q[0] == "?":
            a , b  = map(int,Q[1:])
            print(value[b]-value[a] if findparent(a)==findparent(b) else "UNKNOWN")
        else :
            a , b , w = map(int,Q[1:])
            if findparent(a) != findparent(b):
                union(parent[a] , parent[b] , w-value[b]+value[a])
                        

        