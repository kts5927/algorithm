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

N = int(input())
lst = list(map(str,input().strip()))
compare = ['g','o','r','i']
point = 0
for i in lst:
    if i == compare[point]:
        point += 1
    else:
        point = 0
    if point == 4:
        print('YES')
        break
if point != 4:
    print('NO')