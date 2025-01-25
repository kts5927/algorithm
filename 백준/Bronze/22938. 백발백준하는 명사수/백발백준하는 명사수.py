x,y,d = map(int,input().split())
X,Y,D = map(int,input().split())

if (x-X)**2 + (y-Y)**2 < (d+D)**2:
    print('YES')
else:
    print('NO')