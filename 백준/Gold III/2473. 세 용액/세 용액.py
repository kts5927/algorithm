import sys
N = int(input())
arr = sorted(list(map(int,sys.stdin.readline().split())))

ans = [1000000000,1000000000,1000000000]

for i in range(N-2):
    left = i+1
    right = N-1
    
    while(left<right):
        arrsum = arr[left] + arr[right] + arr[i]
        anssum = sum(ans)
        if(abs(arrsum) < abs(anssum)):
            ans = [arr[left] , arr[right] , arr[i]]
            
        if(arrsum > 0):
            right -= 1
        elif(arrsum < 0):
            left += 1
        elif(arrsum == 0):
            ans.sort()
            print(*ans)
            sys.exit()
ans.sort()
print(*ans)
           