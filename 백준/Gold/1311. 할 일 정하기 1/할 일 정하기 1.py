N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]

dp = {}

def cal(number,work):
    if(number,work) in dp:
        return dp[(number,work)]
    if work == (1 << N) - 1 :
        return 0
    min_cost = int(1e9)
    for i in range(N):
        if work & (1 << i):
            continue
        cost = cal(number+1,work | (1 << i)) + table[number][i]
        min_cost = min(cost,min_cost)
    dp[(number,work)] = min_cost
    return min_cost

print(cal(0,0))