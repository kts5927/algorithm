N = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0
for i in range(1,len(lst)+1):
    for j in lst[:i]:
       ans += j
       
print(ans) 