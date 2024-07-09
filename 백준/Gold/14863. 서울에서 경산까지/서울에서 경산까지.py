import sys

N , K = map(int,sys.stdin.readline().split())

lst1 = []
lst2 = []

for i in range(N):
    a , b , c , d = map(int,sys.stdin.readline().split())
    lst1.append([a,b])
    lst2.append([c,d])
    
    
lst = [[0]*1000000 for _ in range(N)]
lst[0][lst1[0][0]] = lst1[0][1]
lst[0][lst2[0][0]] = max(lst[0][lst2[0][0]] ,lst2[0][1] )
P = max(lst1[0][0] , lst2[0][0])

for i in range(1,N):
    point = P
    for j in range(P + max(lst1[i][0] , lst2[i][0])):
        if lst[i-1][j] != 0:
            lst[i][j+lst1[i][0]] = max(lst1[i][1]+lst[i-1][j],lst[i][j+lst1[i][0]])
            lst[i][j+lst2[i][0]] = max(lst2[i][1]+lst[i-1][j],lst[i][j+lst2[i][0]])  
    P = max(P+lst1[i][0] , P+lst2[i][0])
print(max(lst[-1][:K+1]))