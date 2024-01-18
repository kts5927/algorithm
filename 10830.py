import sys
def matrix(a:list,b:list,n:int): # 행렬곱
    c = []
    for i in range(n):
        row = []
        for j in range(n):
            result = 0
            for k in range(n):
                result += a[i][k] * b[k][j]
            row.append(result)
        c.append(row)
    return c

N , B = map(int,sys.stdin.readline().split())
in_matrix = []
for i in range(N):
    in_matrix.append(list(map(int,sys.stdin.readline().split())))
binary = []

      #단위행렬 구하기
answer = [[0 for j in range(N)] for i in range(N)]
for i in range(N):   
    answer[i][i] = 1
    
while True :     #B를 2진수로 치환
    t = B%2
    if t == 1:
        B = (B-1)//2 
    else: B = B//2
    binary.append(t)
    if B <= 1:
        binary.append(B)
        break


for i in range(len(binary)): #2진수로 바꾼 binary를 이용해서 계산
    if binary[i] == 1:
        answer = matrix(answer,in_matrix,N)
        answer = [[x % 1000 for x in row] for row in answer]
    in_matrix = matrix(in_matrix,in_matrix,N)
    in_matrix = [[x % 1000 for x in row] for row in in_matrix]
    
for row in answer:
    print(*row)
