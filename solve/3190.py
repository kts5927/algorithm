import sys
#sys.stdin.readline().split()
N = int(input())
field = [[0 for j in range(N)] for i in range(N)]
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
for i in range(len(apple)):
    apple[i][0], apple[i][1] = apple[i][1], apple[i][0]


L = int(input())
direction = []
for i in range(L):
    t,d = input().split()
    t = int(t)
    direction.append([t,d])
    
#머리 돌릴 방향    
dx = [1,0,-1,0] # 오,밑,왼,위
dy = [0,1,0,-1]

head = [1,1]
head_direction = 0
body = []
time = 1
while True : 
    body.append([head[0],head[1]])
    head[0] = head[0] + dx[head_direction]
    head[1] = head[1] + dy[head_direction]
    
    if head[0]<1 or head[0]>N or head[1]<1 or head[1]>N : 
        break
    if head in body : 
        break
    if head in apple :
        apple.remove(head)
    else : 
        body.pop(0)
    for i in range(len(direction)):
        if direction[i][0] == time:

            if direction[i][1] == 'D':
                head_direction = (head_direction + 1)%4       
            if direction[i][1] == 'L':   
                head_direction = (head_direction + 3 )%4           
    time+=1
print(time)