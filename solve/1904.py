import sys
n = int(input())
arr = []
a = 1
b = 2
c = 0
t = 0
if n == 1 :
    print(1)
elif n == 2:
    print(2)
else:
    t = 2
    for i in range(n-2):
        c = (a+b)%15746
        a = b
        b = c
        t+=1
    print(c)