n = int(input())
n -=1
A = [[1, 1],
     [1, 0]]

answer = [[1, 0],
          [0, 1]]
MOD = 1000000
result = A

while n != 0:
    if n % 2 == 1:
        temp = [[0, 0],
                [0, 0]]
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(A)):
                    temp[i][j] += answer[i][k] * result[k][j]
        answer = temp
    for i in range(len(A)):
        for j in range(len(A[0])):
            answer[i][j] %= MOD
            result[i][j] %= MOD
    
    temp = [[0, 0],
            [0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A)):
                temp[i][j] += result[i][k] * result[k][j]
    result = temp

    
    
    n = n // 2

print(answer[0][0])
