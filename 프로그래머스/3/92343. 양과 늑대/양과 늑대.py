from collections import deque

ans = 0


def DFS(plan , visited, sheep, wolf, info, node):
    global ans
    print(wolf, sheep)
    
    if len(plan) > 0:
        location = plan.pop()
        if info[location] == 0:
            sheep += 1
        else:
            wolf += 1
        if wolf < sheep:
            ans = max(ans,sheep)
            for i in node[location]:
                if i not in visited:
                    plan.append(i)
                    visited.append(i)
            

            for i in range(len(plan)):
                Plan = plan.copy()
                Visited = visited.copy()
                DFS(Plan,Visited,sheep,wolf,info,node)
                if len(plan) > 0:
                    a = plan.popleft()
                    plan.append(a)
            
        


def solution(info, edges):
    answer = 0
    
    node = [[] for _ in range(len(info))]
    for i in edges:
        node[i[0]].append(i[1])
        node[i[1]].append(i[0])
    
    plan = deque()
    plan.append(0)
    visited = [0]

    DFS(plan , [0], 0, 0, info, node)
    answer = ans
    return answer