# 백준 111 제목 티어 https://www.acmicpc.net/problem/
# 오늘의 잔디 추천 :  https://www.acmicpc.net/problem/
# 1562
# 1019
# 1006 <- 어려움
# https://www.acmicpc.net/problem/16953 그리디
# 낚시왕
# 딕셔너리 , set 꼭 공부하기
# sum 함수는 시간 엄청 잡아먹음
# string to list
# import - heapq
# sort(key = lambda x:x*3 , reverse = True)
# from itertools import permutations


def sharkwave (x , y , speed , direction):
    x_res = x
    y_res = y
    
    if direction == 3 or direction == 4:
        x_move = dx[direction]*speed
        if direction == 3:
            if (x + x_move)%R > 0:
            
                if ((x + x_move)%R)//2 == 0:
                    x_res = (x + x_move)%R
                else:
                    x_res = R - (x+x_move)%R
                    
            else:
                x_res = x + x_move
            
        if direction == 4:
            if (x + x_move)%R < 0:
                if ((x + x_move)%R)%2 == 0:
                    x_res = R - (x + x_move)//R
                else:
                    x_res = (x + x_move)//R
            else:
                x_res = x+x_move
    return x_res , y_res
                
R = 4                
                
dx = [0 , 0 , 0 , 1 , -1]
dy = [0 , 1 , -1 , 0 , 0]

print(sharkwave(1 , 2 , 5 , 3))