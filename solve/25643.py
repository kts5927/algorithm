M , N = map(int,input().split())
lst = []
for i in range(M):
    lst.append(list(map(str,input())))
ans = 0
for i in range(1,M):
    for j in range(1,N+1):
        check = 0
        if lst[i][:j] == lst[i-1][N-j:] or lst[i][N-j:] == lst[i-1][:j]:
            check = 1
            break
            
    if not check:
        print(0)
        exit(0)
print(1)