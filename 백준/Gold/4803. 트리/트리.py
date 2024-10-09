from collections import deque

# Union-Find로 부모 찾기
def union(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = union(parent[x])  # 경로 압축
        return parent[x]

# 두 노드를 합치기
def merge(x, y):
    a = union(x)
    b = union(y)
    if a == b:
        return False  # 사이클이 발생한 경우 False
    parent[b] = a
    return True

# BFS로 사이클이 없는지 확인하면서 탐색
def check(start, visited):
    que = deque([(start, -1)])  # (현재 노드, 직전 노드) 저장
    visited[start] = True
    cycle_check = True  # 사이클 여부를 저장
    
    while que:
        node, prev = que.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if not merge(node, neighbor):  # merge 실패 시 사이클 존재
                    cycle_check = False
                que.append((neighbor, node))  # 현재 노드를 직전 노드로 저장
            # 이미 방문한 노드인데, 직전 노드가 아닌 경우 사이클 존재
            elif neighbor != prev:
                cycle_check = False

    return cycle_check

# 메인 함수: 여러 테스트 케이스를 처리
case_number = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    tree = [[] for _ in range(n+1)]
    
    # 간선 입력
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    visited = [False] * (n + 1)
    parent = [i for i in range(n + 1)]  # Union-Find 부모 초기화
    ans = 0  # 트리의 개수

    # 모든 노드를 탐색하며 트리 여부 확인
    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 노드에서 시작
            if check(i, visited):  # 트리인지 확인
                ans += 1

    # 결과 출력
    if ans == 0:
        print(f'Case {case_number}: No trees.')
    elif ans == 1:
        print(f'Case {case_number}: There is one tree.')
    else:
        print(f'Case {case_number}: A forest of {ans} trees.')
    
    case_number += 1
