T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    A = a**2 + (b+c)**2
    B = b**2 + (a+c)**2
    C = c**2 + (a+b)**2
    
    print(min(A,B,C))