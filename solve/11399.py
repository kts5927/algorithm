N = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0
cal = 0
for i in lst:
    cal += i
    ans += cal
       
print(ans) 