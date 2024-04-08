import sys
M , N = map(int,sys.stdin.readline().split()) 
snack = list(map(int,sys.stdin.readline().split()))
num = len(snack)
snack.sort()
ans = 0
left = 1
right = snack[-1]



while left <= right:
    count = M 
    mid = (left + right) // 2
    
    for i in range(N-1,-1,-1):
        count -= (snack[i] // mid)
        if count <= 0:
            break
    
    if count > 0:
        right = mid-1
    elif count <= 0:
        ans = mid
        left = mid + 1
        
print(ans)