import sys
n = int(input())

if n <= 7:
    print(1)
    sys.exit()
a = 0
while(n >= 0):
    n -= 7
    a += 1
print(a)
