N , A , B = map(int,input().split())

ans = 0
a = min(A,B)
b = max(A,B)
while a != b:
    a = (a+1)//2
    b = (b+1)//2
    ans += 1
print(ans)