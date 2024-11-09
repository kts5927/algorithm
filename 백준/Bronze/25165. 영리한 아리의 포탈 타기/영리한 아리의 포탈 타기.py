N,M = map(int,input().split())
A,D = map(int,input().split())
Sr,Sc = map(int,input().split())

if Sr == N and (N+D)%2 == 1:
    print('YES!')
else:
    print('NO...')