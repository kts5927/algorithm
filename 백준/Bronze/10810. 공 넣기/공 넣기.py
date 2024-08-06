N,M = map(int,input().split())
lst = [0]*N
for i in range(M):
    i,j,k = map(int,input().split())
    for q in range(i,j+1):
        lst[q-1] = k
    
print(*lst)