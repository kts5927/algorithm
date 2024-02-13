N = int(input())
K = int(input())

start = 1
end = N*N
ans = 0

while start <= end:
    count = 0
    mid = (start + end)//2
    for i in range(1,1+N):
        count += min(mid//i , N)
        
    
    if count >= K:
        ans = mid  
        end = mid-1
    else:
        start = mid+1
    
        
print(ans)



