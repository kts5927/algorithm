import sys
input = sys.stdin.readline
N,L,M = map(int,input().split())
Fish = []

def Net(nL):
    half_nL = nL//2
    nets = []
    for i in range(1,half_nL):
        nets.append((i,half_nL-i))
    return nets

def check(y,x,net):
    if y+net[0] > N or x+net[1] > N:
        return False
    else:
        return True
    
def count(y,x,net):
    if not check(y,x,net):
        return 0
    fishcount = 0
    for fy,fx in Fish:
        if y <= fy <= y+net[0] and x <= fx <= x+net[1]:
            fishcount += 1
    return fishcount


def getFish(net):
    maxfish = 0
    for y,x in Fish:
        
        for ny in range(y,y-net[0]-1,-1):
            maxfish = max(maxfish,count(ny,x,net))
        for nx in range(x,x-net[1]-1,-1):
            maxfish = max(maxfish,count(nx,x,net))
    return maxfish
for _ in range(M):
    y,x = map(int,input().split())
    Fish.append((y,x))
    
def solve():
    ans = 0
    for net in Net(L):
        ans = max(ans,getFish(net))
        
    print(ans)
solve()