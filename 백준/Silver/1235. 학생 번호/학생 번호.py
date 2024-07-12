import sys

N = int(sys.stdin.readline())
lst = [str(sys.stdin.readline().strip()) for _ in range(N)]
count = 1
a = len(lst[0]) - 1
b = len(lst[0])

while a >= 0:
    ans = []
    for i in range(N):
        ans.append(lst[i][a:b])
    if len(set(ans)) == N:
        break
    else:
        count += 1
    a -= 1
    
print(count)