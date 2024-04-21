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
import sys


def paper_connect(table:list, paper:list,count:int,visit:list,ans:int):
    
    
    print()
    for i in table:
        print(*i, end = '\n')
    
    print()
    print(paper)
    print(count)
    print(visit)
    print()
    
    
    for i in range(10):
        for j in range(10):
            check = True
            paper_range = min(5, 10-i, 10-j)
            if table[i][j] != 0:
                check = False
                
                for q in range(5):
                    for w in range(5):
                        
                        
                        if i + q < 10 and q < paper_range and w + j < 10 and w < paper_range and table[i+q][w+j] == 0:
                            paper_range = max(q , w)
                        
                            
            if paper_range != 0 and not check and paper[paper_range] > 0:
                if paper[paper_range] == 0:
                    while paper_range>0 and paper[paper_range] != 0:
                        paper_range -= 1
                        
                for q in range(paper_range+1):
                    for w in range(paper_range+1):
                        table[i+q][j+w] = 0
                paper[paper_range] -= 1
                if [i,j,paper_range] not in visit:
                    visit.append([i,j,paper_range])
                    ans = min(ans,paper_connect(table,paper,count+1,visit,ans))
                    visit.remove([i,j,paper_range])
                for q in range(paper_range+1):
                    for w in range(paper_range+1):
                        table[i+q][j+w] = 1
                paper[paper_range]+=1
    zero = True
    for i in range(10):
        for j in range(10):
            if table[i][j] == 1:
                zero = False
    if zero:
        ans = min(ans, count)
    return ans





table = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
paper = [5 for i in range(6)]
visit = []
ans = float('inf')
ans = paper_connect(table,paper,0,visit,ans)
print(ans)