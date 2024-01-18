from itertools import combinations
N,S = map(int,input().split())
arr = list(map(int,input().split()))
case = []
for i in range(len(arr)):
    case.append(list(combinations(arr,i+1)))
count = 0
case = list(case)
for i in range(len(case)):
    for j in range(len(case[i])):
        cal = 0
        
        for k in range(len(case[i][j])):
            cal += case[i][j][k]
        if cal == S:
            count+=1
            
print(count)

