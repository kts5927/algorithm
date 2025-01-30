T = int(input())
lst = list(map(int,input().split()))
prob = [[] for _ in range(len(lst))]
for i in range(T):
    level, time = map(int,input().split())
    prob[level-1].append(time)
for i in prob:
    i.sort()

ans = 0
for i in range(len(lst)):
    
    cal = 0
    for j in range(lst[i]):
        ans += prob[i][j]
    for j in range(1,lst[i]):
        ans += (prob[i][j] - prob[i][j-1])
ans += 60*(len(lst)-1)
print(ans)