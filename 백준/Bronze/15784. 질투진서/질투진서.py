N,a,b = map(int,input().split())
Class = []
for i in range(N):
    Class.append(list(map(int,input().split())))
    
feel = 'HAPPY'
for i in range(N):
    if Class[a-1][i] > Class[a-1][b-1] or Class[i][b-1] > Class[a-1][b-1]:
        feel = 'ANGRY'
        
print(feel)