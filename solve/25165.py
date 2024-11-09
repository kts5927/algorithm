import sys
N,M = map(int,sys.stdin.readline().split())
A,D = map(int,sys.stdin.readline().split())
Sr,Sc = map(int,sys.stdin.readline().split())

if Sr == N and (N+D)%2 == 1:
    print('YES!')
else:
    print('NO...')