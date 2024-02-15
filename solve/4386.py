import sys
n = int(input())
star = [list(map(float,sys.stdin.readline().split())) for _ in range(n)]

distance = []
for i in range(n):
    for j in range(i+1,n):
        if (((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5 != 0):
            distance.append([i+1 , j+1 , ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5])
        
distance.sort(key = lambda x :( x[2] , x[0]))
distance.reverse()
visited = []
for i in range(n+1):
    visited.append(i)
    
ans = 0

while(distance):
    a = distance.pop()
    if visited[a[0]] != visited[a[1]]:
        old_group = visited[a[1]]  
        new_group = visited[a[0]]  
        ans += a[2]

        for i in range(1, n+1):
            if visited[i] == old_group:
                visited[i] = new_group

print(f"{ans:.2f}")

