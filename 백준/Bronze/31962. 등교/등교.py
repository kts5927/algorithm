import sys
input = sys.stdin.readline

N,X = map(int,input().split())
start = -1
for i in range(N):
    a,b = map(int,input().split())
    if a > start and a+b <= X:
        start = a

print(start)