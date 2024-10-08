N , M = map(int,input().split())

lst = [i for i in range(1,N+1)]
for i in range(M):
    a , b = map(int,input().split())
    lst[a-1],lst[b-1] = lst[b-1],lst[a-1]


print(*lst)