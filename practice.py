# 백준 111 제목 티어 https://www.acmicpc.net/problem/

# 1600
import sys
sys.setrecursionlimit(10**5)
N , M , Q = map(int,sys.stdin.readline().split())
tank = list(map(int,sys.stdin.readline().split()))
water = [0 for _ in range(N)]
parent = [i for i in range(N+1)]

def root(a):
    if a != parent[a]:
        parent[a] = root(parent[a])
    return parent[a]

for i in range(N):
    if tank[i] == 0:
        water[i] -= 1
    else : water[i] += 1
    
for i in range(M):
    a , b = map(int,sys.stdin.readline().split())
    A = root(a)
    B = root(b)
    if A != B :
        parent[B] = A
        water[A-1] += water[B-1]

for i in range(Q):
    a = int(sys.stdin.readline())
    A = root(a)
    if water[A-1] > 0:
        print(1)
    else:print(0)