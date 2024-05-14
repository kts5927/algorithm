N , M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

for i in lst:
    if M >= i:
        M += 1
    else:
        break
print(M)
