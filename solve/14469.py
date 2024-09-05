import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort()

time = 0
for i in lst:
    time = max(time,i[0])
    time += i[1]
    
print(time)