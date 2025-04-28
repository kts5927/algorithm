import math
N = int(input())
M = int(input())

N = N**0.5
N = math.ceil(N)
M = M**0.5
ans = 0
Min = int(N)**2

for i in range(int(N),int(M)+1):
    ans += i**2
if ans > 0:        
    print(ans)
    print(Min)
else:
    print(-1)