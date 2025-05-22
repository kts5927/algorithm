N = int(input())
ans = 0
for i in range(N):
    good = list(map(str,input().strip()))
    stack = ['0']
    for i in good:
        if stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    if stack == ['0']:
        ans += 1
print(ans)