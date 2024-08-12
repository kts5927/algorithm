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

import sys;input=lambda:sys.stdin.readline().strip('\n')
MIS = lambda: map(int,input().split())

n, m, x, y = MIS()
adj = [set() for i in range(n+1)]
for i in range(m):
    a, b = MIS()
    adj[a].add(b)
    adj[b].add(a)
pos = {x}
for i in range(y):
    npos = set()
    for x in pos: npos|= adj[x]
    pos = npos

if pos: print(*sorted(pos))
else: print(-1)
