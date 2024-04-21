import sys
table = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
paper = [5 for i in range(6)]
ans = float('inf')
result = set()

def paper_connect(table:list, paper:list,count:int,ans:int):

    for i in range(10):
        for j in range(10):
            
            if table[i][j] != 0:
                
                for k in range(5):
                    check = True
                    if paper[k+1] == 0:
                        continue
                    if i+k >= 10 or j + k >= 10:
                        continue
                    for q in range(k+1):
                        for w in range(k+1):
                            if table[i+q][j+w] == 0:
                                check = False
                                break
                        if not check:
                            break
                            
                    if check:
                        for q in range(k+1):
                            for w in range(k+1):
                                table[i+q][j+w] = 0
                        paper[k+1] -= 1
                        result.add(paper_connect(table,paper,count+1,ans))
                        paper[k+1]+=1
                        for q in range(k+1):
                            for w in range(k+1):
                                table[i+q][j+w] = 1
                if result :
                    return min(result)
                else:
                    return -1
    return count
                        

result.add(paper_connect(table,paper,0,ans))
if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)


# 종료값 문제
