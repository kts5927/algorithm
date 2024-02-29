table = [[0 for _ in range(20)]for _ in range(20)]
table[0][0] = 1
for i in range(1,20):
    for j in range(i+1):
        table[i][j] = table[i][j-1] + table[i-1][i-j]
           
ans = []
for _ in table:
    ans.append(sum(_)*2)
    
ans[0] = 1
N = int(input())
for i in range(N):
    print(ans[int(input())-1])
    
# Euler Zigzag Number (Entringer Number)
# E(n,k)=E(n,k-1)+E(n-1,n-k)(E(0,0)=1,E(m,0)=0)

 

