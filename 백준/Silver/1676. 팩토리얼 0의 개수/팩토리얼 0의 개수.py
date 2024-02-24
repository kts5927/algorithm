N = int(input())
count = 0
for i in range(1,N+1):
    a = i
    while a%5 == 0:
        a = a//5 
        count +=1
print(count)