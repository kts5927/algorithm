N = int(input())
cost = list(map(str,input().split()))
M = int(input())

table = [[[] for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(M+1):

        if j - int(cost[i-1]) >= 0 :
            if table[i-1][j] == []:
                print(table[i-1][j])
                table[i-1][j] += table[i][j-int(cost[i-1])]

for i in table:
    print(*i, end='\n')
        # int(''.join(table[i-1][j])) > int(''.join(table[i-1][j-cost[i-1]] + [str(i-1)])):
        #     print(0)