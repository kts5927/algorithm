numbers = list(map(int,input().split()))

odd = []
even = []

for i in numbers:
    if i%2 == 1:
        odd.append(i)
    else:
        even.append(i)
        

ans = 1
        
if len(odd) > 0:
    for i in odd:
        ans *= i
    print(ans)
else:
    
    for i in even:
        ans *= i
    print(ans)