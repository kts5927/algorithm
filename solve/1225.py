a , b = map(str,input().split())
A = list(map(int,a.strip()))
B = list(map(int,b.strip()))

ans = 0
for i in A:
    for j in B:
       ans += i*j
       
print(ans) 