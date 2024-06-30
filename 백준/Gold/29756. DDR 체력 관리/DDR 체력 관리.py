import sys
sys.setrecursionlimit(10000)  # 재귀 한도 설정

def cal(num, hp):
    if num == 0:
        return 0

    cal_hp = min(hp + K, 100)
    if dp[num][cal_hp] != 0:
        return dp[num][cal_hp]
    
    ans = cal(num - 1, cal_hp)
    if (cal_hp - lst_2[num]) >= 0:
        ans = max(ans, cal(num - 1, cal_hp - lst_2[num]) + lst_1[num])
    
    dp[num][cal_hp] = ans
    return ans

N, K = map(int, input().split())
lst_1 = [0] + list(map(int, input().split()))  # 0번째 인덱스에 0을 추가하여 1부터 시작
lst_2 = [0] + list(map(int, input().split()))  # 0번째 인덱스에 0을 추가하여 1부터 시작

dp = [[0] * 101 for _ in range(N + 1)]  # DP 배열 초기화

print(cal(N, 100))
