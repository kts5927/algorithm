import sys
N = int(sys.stdin.readline())

lst = []
MAX = 0
while True:
    Input = list(map(int,sys.stdin.readline().split()))
    
    if len(Input) == 1 and Input[0] == -1:
        break
    else:
        MAX = max(MAX,max(Input)) 
        lst.append(Input)

cal = [0 for _ in range(MAX+1)]
for i in lst:
    for j in i[1:]:
        cal[j] = i[0]

ans = []
while N != 0:
    ans.append(N)
    N = cal[N]

print(*ans)
    