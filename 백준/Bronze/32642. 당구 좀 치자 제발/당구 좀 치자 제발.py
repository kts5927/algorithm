import sys
input = sys.stdin.readline
N = int(input())
weather = list(map(int,input().split()))

aggressive = 0
ans = 0

for rain in weather:
    if rain == 0:
        aggressive -= 1
    else:
        aggressive += 1
        
    ans += aggressive
    
print(ans)
