import math

a, b = map(int,input().split())
cal = []


print(''.join('1')*math.gcd(a,b))