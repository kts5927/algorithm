dp = [1]*2001
dp[0] = 0
dp[1] = 0
n = 2
while n < 2001:
    if dp[n] == 1:
        i = 2
        while n*i < 2001:
            if n*i < 20002 and dp[n*i] == 1:
                dp[n*i] = 0
            i += 1
    n += 1


def calculation(first : list, second:list):
    ret = 0
    for i in range(len(first)):
        for j in range(len(second)):
            if dp[first[i] + second[j]] == 1:
                if len(first) > 1 and len(second) > 1:
                    ret = max(ret, calculation(first[0:i] + first[i+1:len(first)], second[0:i] + second[i+1:len(second)]))
                else:
                    return 1
            if ret == 1:
                return ret
        if ret == 1:
            return ret
    return ret



N = int(input())
lst = list(map(int,input().split()))
lst_len = len(lst)

ans = []

first = []
second = [] 
for i in range(len(lst)):
    if lst[i]%2 == 1:
        first.append(lst[i])
    if lst[i]%2 == 0: 
        second.append(lst[i])

if len(first) != len(second):
    print(-1)
else:

    if lst[0]%2 == 1:
        for i in range(len(second)):
            if calculation(first[1:], second[0:i] + second[i+1:len(second)]):
                ans.append(second[i])

    if lst[0]%2 == 0:
        for i in range(len(second)):
            if calculation(first[1:] + first[i+1:len(first)], second[0:]):
                ans.append(first[i])
                
    ans.sort()
    if len(ans) != 0:
        print(*ans)
    else : 
        print(-1)


    # 시간초과 : 이분매칭 / 최대유량 공부하기

