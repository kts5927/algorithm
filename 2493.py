#이전 탑 보다 작은 탑이 나왔을때, 이전탑의 x좌표 출력, 높이와 x좌표를 스택에 추가
#이전 탑 보다 큰 탑이 나오면, 앞의 탑들과 비교해서 자신의 크기 이상인 탑의 x좌표 출력, 사이에 있는 스택들 전부 pop, 높이와 x좌표를 스택에 추가
#만약에 이전탑보다 큰데 자기보다 더 큰 이전탑이 없으면 0 출력

N = int(input())
tower = list(map(int, input().split()))
answer = []
tower_collection = []

for i in range(N):
    while tower_collection and tower[i] > tower[tower_collection[-1][1]]:
        tower_collection.pop()

    if not tower_collection:
        answer.append(0)
    else:
        answer.append(tower_collection[-1][1] + 1)

    tower_collection.append([tower[i], i])

print(*answer)