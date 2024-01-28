import sys
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    a , b = map(int,sys.stdin.readline().split())
    arr.append([a,b])
    
arr.sort(key = lambda x:(x[1],x[0]))
time = 0
count = 0
for start,end in arr:
    if time <= start:
        count+=1
        time = end
print(count)