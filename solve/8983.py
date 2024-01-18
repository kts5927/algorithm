import sys
M,N,L = map(int,input().split())
gun_lit = list(map(int,input().split()))
animals = []
for i in range(N):
     animals.append(list(map(int,input().split())))
wanted = [False]*N
for i in range(M):
    for j in range(N):
        if wanted[j] !=True:
            if L>=(abs(gun_lit[i]-animals[j][0])+animals[j][1]):
                wanted[j] = True

print(wanted.count(True))