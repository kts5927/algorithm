a = int(input())
prime_number = list(map(int,input().split()))
result = 0

for x in prime_number:
    if x>1:
        count = 0
        for i in range(2,x):
            if x % i == 0:
                count+=1
        if count == 0:
            result+=1    
        
print(result)
