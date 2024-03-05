N , S = map(int,input().split())
numbers = list(map(int,input().split()))

start = 0
end = 0
ans = float('inf')
sum = numbers[0]
while start <= end:
    if sum >= S :
        ans = min(ans , end-start+1)
        sum -= numbers[start]
        start +=1 
    elif sum < S:
        end += 1
        if end <N:
            sum += numbers[end]
        else : break
        

if ans != float('inf'):            
    print(ans)
else : print(0)
