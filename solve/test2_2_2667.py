import sys

N = int(sys.stdin.readline())
buildings = []
aa = []
aa.append(0)
def calculate(buildings,count,shadow,i,j,N):
    

    if i > 0 and buildings[i-1][j] == 1 and shadow[i-1][j] == 0:
        shadow[i-1][j] = count
        aa[count] += 1
        calculate(buildings,count,shadow,i-1,j,N)
    if i < N-1 and buildings[i+1][j] == 1 and shadow[i+1][j] == 0:
        shadow[i+1][j] = count
        aa[count] += 1
        calculate(buildings,count,shadow,i+1,j,N)   
    if j > 0 and buildings[i][j-1] == 1 and shadow[i][j-1] == 0:
        shadow[i][j-1] = count
        aa[count] += 1
        calculate(buildings,count,shadow,i,j-1,N)   
    if j < N-1 and buildings[i][j+1] == 1 and shadow[i][j+1] == 0:
        shadow[i][j+1] = count
        aa[count] += 1
        calculate(buildings,count,shadow,i,j+1,N)   
    


for i in range(N):
    a = list(map(int,sys.stdin.readline().strip()))
    buildings.append(a)

shadow = [[0 for _ in range(N)] for _ in range(N)]
count = 1
for i in range(N):
    for j in range(N):
        if buildings[i][j] != 0 and shadow[i][j] == 0:
            shadow[i][j] = count
            
            aa.append(1)
            calculate(buildings,count,shadow,i,j,N)
            count+=1
            
print(count - 1)
aa.sort()
for i in range(1,count ):
    print(aa[i])