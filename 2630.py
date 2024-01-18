import sys
input = sys.stdin.readline



n = int(input())
table= [list(map(int,input().split())) for _ in range(n)]
answer = [0,0]
def paper_check(x:int,y:int,length:int):
    color = table[x][y]
    for i in range(x,length+x):
        for j in range(y,length+y):
            if color != table[i][j]:
                paper_check(x,y,length//2)
                paper_check(x+length//2,y,length//2)
                paper_check(x,y+length//2,length//2)
                paper_check(x+length//2,y+length//2,length//2)
                return 0
    if color == 0:
        answer[0] +=1
    else :answer[1]+=1    
  
  
  
        
paper_check(0,0,n)
for i in answer:
    print(i)