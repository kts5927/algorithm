N = int(input())
count = 0
ans = N
while True:
    cal = (ans-ans%10)//10 + ans%10
    ans = cal%10 + ans%10*10
    count+=1
    if N == ans:
        break
    
    
print(count)