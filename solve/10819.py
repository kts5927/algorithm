from itertools import permutations

N = int(input())
lst = list(map(int,input().split()))

cal = list(permutations(lst,N))
ans = 0
for i in cal:
    sum_ = 0
    for j in range(1,len(i)):
        a = i[j]
        b = i[j-1]
        sum_ += abs(a - b)
    if sum_ >= ans:
        ans = sum_
print(ans)