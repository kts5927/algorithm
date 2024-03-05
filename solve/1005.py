import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    
    N , K = map(int,sys.stdin.readline().split())
    
    build_time = list(map(int,sys.stdin.readline().split())) # 건물 짓는데 걸리는 시간
    build_time.insert(0,0) # 위치 맞추기
    sequence = [[] for _ in range(N+1)] # 건물의 태크트리
    tech = [0 for _ in range(N+1)] # 이전 테크트리를 모두 만족했는지? => 위상정렬
    for __ in range(K):
        before , after = map(int,sys.stdin.readline().split())
        tech[after] +=1
        sequence[before].append(after)
    W = int(sys.stdin.readline()) # 이기기 위해 필요한 건물의 번호
    
    build = []
    for i in range(1,N+1):
        if tech[i] == 0:
            heapq.heappush(build, [build_time[i],i])
    
    complete = [False for _ in range(N+1)]
 
    time = 0       
    finish_ = True
    while True:
        if build[0][0] != 0:
            time += 1
        if build[0][0] != 0:
            for i in build:
                i[0] -= 1
        
        
        while build[0][0] == 0:
            b_time , number = heapq.heappop(build)
            for j in sequence[number]:
                tech[j] -= 1
                if tech[j] == 0:
                    heapq.heappush(build,[build_time[j],j])
                    
            if not build  and tech[W] == 0 and b_time == 0 and number == W: 
                print(time)
                finish_ = False
                break
            
        
        if finish_:
            if tech[W] == 0 and b_time == 0 and number == W:
                print(time)
                break
        else : break
        

# 1
# 4 4
# 0 0 0 0
# 1 2
# 1 3
# 2 4
# 3 4
# 4

# 1
# 4 4
# 1 1 0 0
# 1 2
# 1 3
# 2 4
# 3 4
# 4

# 1
# 4 4
# 0 0 1 1
# 1 2
# 1 3
# 2 4
# 3 4
# 4