T = int(input())
maxY = -float('inf')
minY = float('inf')

for i in range(T):
    x,y = map(int,input().split())

    maxY = max(y,maxY)
    minY = min(y,minY)
    
print(maxY - minY)