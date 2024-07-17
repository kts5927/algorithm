while True:
    a , b , c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    if max(a,b,c) >= a+b+c - max(a,b,c):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a != b and a != c and b != c:
        print('Scalene')
    else:
        print('Isosceles')

