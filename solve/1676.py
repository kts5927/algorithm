N = int(input())
a = 0
for i in range(1,N+1): 
    while i%5 == 0: 
        i = i//5 
        a +=1
print(a)

# t=int(input())//5
# print(t+t//5+t//25)