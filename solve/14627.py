import sys
input = sys.stdin.readline

S , C = map(int,input().split())
onion = []
for i in range(S):
    onion.append(int(input()))

L = 1
R = max(onion)
ans = 0
while L <= R:
    
    mid = (L + R) // 2
    use = sum(o // mid for o in onion)
    if use < C:
        R = mid-1
    else:
        ans = max(ans,mid)
        L = mid+1
print(use, mid)

print(sum(onion) - (ans*C))     