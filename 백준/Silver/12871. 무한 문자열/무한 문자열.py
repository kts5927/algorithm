from math import lcm

def sol():
    a = list(map(str,input().strip()))
    b = list(map(str,input().strip()))

    A = len(a)
    B = len(b)
    LCM = lcm(A,B)
    a = a*(LCM//A)
    b = b*(LCM//B)
    
    if a != b:
        return 0
    else:
        return 1
print(sol())
        