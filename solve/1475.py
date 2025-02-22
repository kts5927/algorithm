lst = [0 for _ in range(9)]
N = input()
for n in N:
    if int(n) == 6 or int(n) == 9:
        lst[6] += 1
    else:
        lst[int(n)] += 1
        
ans = 0

for i in range(9):
    if i == 6:
        ans = max(ans,(lst[i]+1)//2)
    else:
        ans = max(ans,lst[i])
print(ans)