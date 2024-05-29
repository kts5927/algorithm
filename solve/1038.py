from itertools import combinations

N = int(input())
cal = []

for i in range(1,11):
    for j in combinations(range(10),i):
        num = ''.join(list(map(str,reversed(list(j)))))
        cal.append(int(num))
cal.sort()
if N >= len(cal): 
    print(-1)      
else:   
    print(cal[N])