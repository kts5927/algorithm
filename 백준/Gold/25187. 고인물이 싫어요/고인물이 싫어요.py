import sys
sys.setrecursionlimit(10**5)
N , M , Q = map(int,sys.stdin.readline().split())
tank = list(map(int,sys.stdin.readline().split()))
water = [0 for _ in range(N)]
parent = [i for i in range(N+1)]
size = [0] * (N + 1) 

def root(a):
    if a != parent[a]:
        return root(parent[a])
    return parent[a]

def union(a,b):
    a = root(a)
    b = root(b)
    if a>b:
        parent[a] = b
        water[b-1] += water[a-1]
    elif a<b:
        parent[b] = a
        water[a-1] += water[b-1]
        
for i in range(N):
    if tank[i] == 0:
        water[i] -= 1
    else : water[i] += 1


for i in range(M):
    a , b = map(int,sys.stdin.readline().split())
    union(a,b)

for i in range(Q):
    a = int(sys.stdin.readline())
    A = root(a)
    if water[A-1]>0:
        print(1)
    else:print(0)