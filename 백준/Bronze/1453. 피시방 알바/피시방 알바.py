import sys
input = sys.stdin.readline

pc = [0 for i in range(101)]
N = int(input())
customer = list(map(int,input().split()))
ans = 0
for i in customer:
    if pc[i] == 0:
        pc[i] = 1
    else:
        ans += 1
print(ans)