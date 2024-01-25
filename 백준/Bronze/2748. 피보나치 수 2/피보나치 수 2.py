import sys
n = int(input())
t = 0
n1 = 1
n2 = 1
n3 = 0
if n == 1:
    print(n1)
elif n == 2:
    print(n1)
else:
    while t != n-2:
        t+=1
        n3 = n1+n2
        n1 = n2
        n2 = n3
        
    print(n3)    
    