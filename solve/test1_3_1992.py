import sys
input = sys.stdin.readline

n = int(input())
table= [list(map(int,input().strip())) for _ in range(n)]
answer = []
def paper_check(x:int,y:int,length:int):
    color = table[x][y]
    for i in range(x,length+x):
        for j in range(y,length+y):
            if color != table[i][j]:
                answer.append('(')
                paper_check(x,y,length//2)
                paper_check(x,y+length//2,length//2)
                paper_check(x+length//2,y,length//2)
                paper_check(x+length//2,y+length//2,length//2)
                answer.append(')')
                return 
    answer.append(str(color))
  ## 정답 예시
  #(110(0101))(0010)1(0001))
  #11110000
  #11110000
  #00011100
  #00011100
  #11110000
  #11110000
  #11110011
  #11110011
  
        
paper_check(0,0,n)
print("".join(answer))