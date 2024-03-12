string = list(map(str , input().strip()))
dp = [float('inf') for _ in range(len(string) + 1)]

def palin(first , second):
    while first < second:
        if string[first] != string[second-1]:
            return False
        first , second = first+1 , second-1
    return True

dp[0] = 0

for i in range(1 , len(string)+1):
    for j in range(i):
        if palin(j , i):
            dp[i] = min(dp[j] + 1 , dp[i])
print(dp[-1])
