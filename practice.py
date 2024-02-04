import sys
num = int(input())
city = []
for i in range(num):
    city.append(list(map(int, sys.stdin.readline().split())))
def TSP(N): # 시작 도시 번호 0 ~ N-1
    city_flag = 0b0
    dp = {}  # key = (start, city_flag)
    '''
    n=3
    bin(city_flag | (1 << n)) <- n자리에 1 추가
    bin(city_flag ^ (1 << n)) <- n자리 끄고 켜기
    bin(city_flag & (1 << n)) <- n자리 1인지 아닌지 값이 0이면 0 1이상이면 1
    '''
    start_city = 0
    def go(start, arr, count, cost, city_flag): # 출발, 도착하는 도시, 몇 번째 방문인지, 그 동안의 비용
        cost += city[start][arr]
        if count >= N - 1: #city_flag == (1 << (N-1)) - 1: # 마지막 방문이면
            if city[arr][start_city] == 0:
                return int(1e9)
            else:
                cost += city[arr][start_city] # 돌아가는 비용 계산
                print(f'return cost={cost}')
                return cost
        if (start, bin(city_flag)) in dp:
            print('dp ret')
            return dp[(start, bin(city_flag))]
        min_cost = int(1e9)
        for i in range(N):
            if city_flag & (1 << i):#not city_flag & (1 << i): # 아직 방문하지X
                continue
            else:
                if city[arr][i] > 0: # 길이 존재
                    city_flag = city_flag ^ (1 << i)
                    cur_cost = go(arr, i, count+1, cost, city_flag)
                    if min_cost > cur_cost:
                        min_cost = cur_cost
        dp[(arr, bin(city_flag))] = min_cost
        city_flag = city_flag ^ (1 << i)
        return min_cost
    min_c = int(1e9)
    for i in range(N):
        city_flag = city_flag ^ (1 << i)
        start_city = i
        for j in range(N):
            if city_flag & (1 << j): #not city_flag & (1 << j):
                continue
            else:
                if city[i][j] != 0: # 길이 있는 도시면
                    city_flag = city_flag ^ (1 << j)
                    min_c = min(min_c, go(i, j, 1, 0, city_flag))
                    city_flag = city_flag ^ (1 << j)
        city_flag = city_flag ^ (1 << i)
    print(dp)
    return min_c
print(TSP(num))