# 백준 111 제목 티어 https://www.acmicpc.net/problem/

# 1562
# 1019
# 1006
# https://www.acmicpc.net/problem/16953 그리디


# import sys
# from collections import deque
# N , M , K = map(int,sys.stdin.readline().split())
# wall = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
# shadow = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K)]
# location = deque()
# location.append([0 , 0 , 0 , 0])

# dx = [1 , -1 , 0 , 0]
# dy = [0 , 0 , 1 , -1]
# while location:
#     i , j , k , count= location.popleft()
#     shadow[k][j][i] = True
#     if i == M-1 and j == N-1:
#         print(count)
#         break	
	
#     for a in range(4):
#         x = dx[a] + i
#         y = dy[a] + j
		
#         if 0 <= x < M and 0 <= y < N and not shadow[k][y][x]:
#             print(x , y , count , k)
#             if wall[x][y] == 0 :
#                 location.append([x , y , k , count + 1 ])
			
#             elif wall[x][y] == 1 and k < K-1:
#                 print('here!')
#                 location.append([x , y , k+1 , count + 1])


from collections import defaultdict

def max_independent_set(graph, n, start=1):
    visited = [False] * (n + 1)
    visited[start] = True
    independent_set = set([start])
    stack = [start]

    while stack:
        curr = stack.pop()
        for neighbor in graph[curr]:
            if not visited[abs(neighbor)]:
                visited[abs(neighbor)] = True
                if neighbor > 0:
                    independent_set.add(neighbor)
                    stack.append(neighbor)

    return independent_set

def soln(n, m, votes):
    graph = defaultdict(list)
    for a, b in votes:
        graph[-a].append(b)
        graph[-b].append(a)

    independent_set = max_independent_set(graph, n)
    if 1 in independent_set:
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        votes = []
        for _ in range(m):
            a, b = map(int, input().split())
            votes.append((a, b))
        print(soln(n, m, votes))