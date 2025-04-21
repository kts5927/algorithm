N,B = map(str,input().split())
N = list(map(str,N.strip()))
B = int(B)
ans = 0

for i in N:
    if ord('0') <= ord(i) <= ord('9'):
        ans += int(i)
    else:
        ans += (ord(i)-ord('A') + 10)
    ans *= B
print(ans//B)