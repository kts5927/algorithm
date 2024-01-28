import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    arr = []
    count = 0
    for _ in range(N):
        a,b = map(int,sys.stdin.readline().split())
        arr.append([a,b])
    arr.sort(key = lambda x : (x[0] , x[1]))   
    max_ = arr[0][1]
    for first,second in arr:
        
        if second <= max_:
            count+=1
            max_ = second
    print(count)
    
