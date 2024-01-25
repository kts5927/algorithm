import sys
first = list(str(sys.stdin.readline().strip()))
second = list(str(sys.stdin.readline().strip()))
LCS = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)] ## first = x , second = y
first.insert(0,'1')
second.insert(0,'2')

for i in range(1,len(first)):
    for j in range(1,len(second)):
        if first[i] == second[j] :
            LCS[i][j] = LCS[i-1][j-1] + 1
        elif first[i] != second[j] :
            LCS[i][j] = max(LCS[i-1][j] , LCS[i][j-1])
            
print(LCS[-1][-1])