import sys

M , n = map(int,sys.stdin.readline().split())
l = [0,0]
direction = [[0,1],[1,0],[0,-1],[-1,0]]
D = 0
FALSE = True
for i in range(n):
    S , N = map(str,sys.stdin.readline().split())
    if str(S) == "TURN":
        if int(N) == 1:
            D = (D + 3)%4
        else:
            D = (D + 1)%4
            
    else:
        l[0] += direction[D][0]*int(N)
        l[1] += direction[D][1]*int(N)
        if l[0] < 0 or l[0] > M or l[1] < 0 or l[1] > M:
            print(-1)
            FALSE = False
            break
if FALSE:
    print(l[1],l[0])