# 백준  https://www.acmicpc.net/problem/
import sys
N = int(input())
for i in range(N):
    arr = list(map(str,input().strip()))
    ans = []
    br = True
    for j in arr:
        if j == '(':
            ans.append(j)
        elif j == ')':
            if len(ans) == 0:
                print('NO')
                br = False
                break
            else : ans.pop()
    if br:
        if len(ans) == 0:
            print('YES')
        else : print('NO')