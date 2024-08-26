import sys

def GCD(a , b):
    while(b > 0):
        a , b = b,a%b
    return a

def LCM(a,b):
    cal = GCD(a,b)
    
    return (a*b)//cal
    

N , D = map(int,sys.stdin.readline().split())
lst = []
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
    
ans = 0
ind = []
for i in range(N):
    for j in range(i+1,N):
        lcm = LCM(lst[i][1],lst[j][1])
        start = max(lst[i][0],lst[j][0])
        
        A = (D-lst[i][0])//lst[i][1] + 1
        B = (D-lst[j][0])//lst[j][1] + 1
        C = D//lcm + 1 - (start+lcm - 1)//lcm
        
        
        
        if ans < A+B-C:
            ans = A+B-C
            ind= [[i+1,j+1]]
        elif ans == A+B-C:
            ind.append([i+1,j+1])
ind.sort()
print(*ind[0])
print(ans)

