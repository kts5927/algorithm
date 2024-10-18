class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 각 노드는 자기 자신을 부모로 초기화
        self.rank = [0] * n  # 트리의 높이(랭크) 저장
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # 경로 압축
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # 트리의 높이가 낮은 쪽을 높은 쪽에 붙인다 (랭크에 따라 union)
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 크루스칼 알고리즘 구현
def kruskal(graph, V):
    # 결과 저장 (MST에 포함된 간선)
    mst = []
    
    # 간선을 가중치 기준으로 정렬
    edges = sorted(graph, key=lambda x: x[2])

    # 유니온-파인드 자료 구조 초기화
    uf = UnionFind(V)

    # 간선들을 순회하면서 MST 구성
    for u, v, weight in edges:
        # u와 v가 같은 트리에 속해 있지 않으면, 간선을 추가하고 union
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    
    return mst

# 그래프 표현: (출발 노드, 도착 노드, 가중치) 형태로 간선 정보 저장
graph = [
    (0, 1, 2),  # 0번 노드에서 1번 노드로 가는 가중치 2
    (0, 3, 6),  # 0번 노드에서 3번 노드로 가는 가중치 6
    (1, 3, 8),  # 1번 노드에서 3번 노드로 가는 가중치 8
    (1, 2, 3),  # 1번 노드에서 2번 노드로 가는 가중치 3
    (2, 3, 5),  # 2번 노드에서 3번 노드로 가는 가중치 5
    (2, 4, 7),  # 2번 노드에서 4번 노드로 가는 가중치 7
    (3, 4, 9)   # 3번 노드에서 4번 노드로 가는 가중치 9
]

# 노드의 개수
V = 5

# 크루스칼 알고리즘을 사용하여 최소 신장 트리를 구합니다.
mst = kruskal(graph, V)

# 결과 출력
print("최소 신장 트리의 간선들:")
for u, v, weight in mst:
    print(f"({u}, {v}) - 가중치: {weight}")