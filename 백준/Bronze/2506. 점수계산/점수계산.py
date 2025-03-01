N = int(input())
lst = list(map(str,input().split('0')))

ans = 0
for i in lst:
    one = i.count('1')
    ans += one*(one+1)//2
print(ans)