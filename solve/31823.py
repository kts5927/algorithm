N,M = map(int,input().split())
Set = []
ans = []
for i in range(N):
    lst = list(map(str,input().split()))
    
    if lst[0] == '.':
        count = 1
    else:
        count = 0
    cal = 0
    for j in range(1,len(lst)):
        if lst[j] == '*':
            cal = max(cal,count)
            count = 0
        elif lst[j] == '.':
            count += 1
            
        else:
            cal = max(cal,count)
            Set.append(cal)
            ans.append([cal,*lst[j:]])
            break
        
Set = set(Set)
print(len(Set))
for i in ans:
    print(*i)