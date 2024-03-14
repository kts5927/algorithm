import sys

def B_search(a , b):
    left = a
    right = b
    while left <= right:
        
        res = 0
        mid = (left + right)//2
        
        for i in Lan:
            res += i//mid
        if res < N:
            right = mid-1
        if res >= N:
            left = mid+1
    return right



K , N = map(int,sys.stdin.readline().split())
Lan = []
for i in range(K):
    Lan.append(int(sys.stdin.readline()))
    
A = max(Lan)
ans = B_search(1 , A)
print(ans)

