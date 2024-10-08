lst = [[0]*101 for _ in range(101)]

N = int(input())

ans = [0]*102
for k in range(N):
    a,b,c,d = map(int,input().split())
    
    for i in range(c):
        for j in range(d):
            ans[k+1] += 1
            ans[lst[i+a][j+b]] -= 1
            lst[i+a][j+b] = k+1
            
for i in range(N):
    print(ans[i+1])