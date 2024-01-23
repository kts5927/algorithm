import sys
from collections import deque
p,k = map(int,sys.stdin.readline().split())
arr = []
for i in range(p):
    a = int(sys.stdin.readline().strip())
    arr.append(a)
arr.sort(reverse = True)
q = [k,0]
number = deque([q])
rute = True
past = set()
while rute:
    if len(number) == 0:
        print('-1')
        rute = False
        break
    n,count = number.popleft()
    for i in arr:
        if  n-i > 0 and n-i not in past:
            number.append([n-i , count+1])
            past.add(n-i)
        
        elif n == i : 
            count+=1
            print(count)
            rute = False
            break