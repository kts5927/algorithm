import copy
from collections import deque

N , K = map(int,input().split())
N = str(N)
str_ = list(map(str , N.strip()))
length = len(N)
arr = deque()
arr.append([str_ , 0])
past = set()
ans = []
while arr:
    string , num = arr.popleft()
    if num == K:
        string = "".join(string)
        ans.append(int(string))
        continue
    for i in range(length):
        for j in range(i+1 , length):
            cal = copy.deepcopy(string)
            cal[i] , cal[j] = cal[j] , cal[i]
            if cal[0] != '0':    
                a = "".join(cal)
                if ((a,num+1)) not in past:
                    past.add((a,num+1))
                    arr.append([cal,num+1])

if ans:
    ans.sort()
    print(ans[-1])
else:print(-1)