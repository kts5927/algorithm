N = int(input())
lst = list(map(int,input().split()))
count = 0
for i in lst:
    if i%10 == N:
        count += 1
        
print(count)