N , K = map(int,input().split())
lst = list(map(int,input().split(',')))

for i in range(K):
    for j in range(len(lst)-1):
        lst[j] = lst[j+1] - lst[j]
    lst = lst[:-1]
    

ans = []
for i in lst:
    ans.append(str(i))
    ans.append(',')

print(''.join(ans[:-1]))