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

T = int(input())
for _ in range(T):
    N = int(input())
    K = 0
    D = 0
    A = 0
    Mission = []
    for i in range(N):
        Mission.append(list(map(int,input().split())))
        
    k,d,a = map(int,input().split())
    
    money = 0
    for i in Mission:
        mission = k*i[0] - d*i[1] + a*i[2]
        if  mission > 0:
            money += mission
    print(money)