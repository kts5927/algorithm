import sys

N , M = map(int,sys.stdin.readline().split())

cal = []
for i in range(N):
    lst = list(map(int,sys.stdin.readline().split()))
    cal.append(lst[1])
    cal.append(lst[-1])
    
cal.sort()
print(cal[N-1])