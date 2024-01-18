number,n,bubble = map(int,input().split())

binary = []
while True:
    if n == 1:
        break
    if n%2 == 0:
        binary.append(False)
    else:binary.append(True)
    n = n // 2
    
    
cal = number%bubble
ans = cal
for i in binary[::-1]:
    if i :  ans = ans**2*cal
    else : ans = ans**2
    ans = ans%bubble
print(ans)