# 백준 111 제목 티어 https://www.acmicpc.net/problem/
# 오늘의 잔디 추천 :  https://www.acmicpc.net/problem/
# 1562
# 1019
# 1006 <- 어려움
# 1082
# https://www.acmicpc.net/problem/16953 그리디
# 낚시왕
# 딕셔너리 , set 꼭 공부하기
# sum 함수는 시간 엄청 잡아먹음
# string to list
# import - heapq
# sort(key = lambda x:x*3 , reverse = True)
# from itertools import permutations
# print(3%2)

import sys

def fail(p):
    m, j = len(p), 0
    l = [0]*m
    for i in range(1, m):
        while j > 0 and p[i]!=p[j]:
            j = l[j-1]
        if p[i] == p[j]:
            j+=1
            l[i] = j
    return l
    
# test1 = 'winlose???winl???w??'
# test2 = 'win'
# test1 = '???cab?????'
# test2 = 'abcab'
# test1 = 'glo?yto?e??an?'
# test2 = 'or'


lst1 = list(map(str,sys.stdin.readline().rstrip()))
lst2 = list(map(str,sys.stdin.readline().rstrip()))
l1_len = len(lst1)
l2_len = len(lst2)
dp = [[0 for _ in range(l1_len)] for _ in range(l2_len+1)]

# print(lst1)
# print(lst2)

for i in range(l2_len):
    for j in range(l1_len):
        if lst1[j] == lst2[i]:
            dp[i][j] = i+1
            dp[-1][j] = 1
        if lst1[j] == '?':
            dp[i][j] = i+1

cal = fail(lst2)


# for i in dp:
#     print(i)
    
    
ans = 0
i = 0
while i <= l1_len-l2_len:
    x = i
    y = 0
    if dp[y][x] == 1:
        while y < l2_len:
            if dp[y][x] == l2_len:
                i = x+1
                y = cal[y-1]
                ans+=1
                break
                
            if dp[y][x] != 0:
                x+=1
                y+=1
            else:
                i+=1
                x = cal[y-1]
                break
    else:
        i+=1
            
print(ans)