import sys
import bisect

HI, ARC = map(int,sys.stdin.readline().split())

HI_List = list(map(int,sys.stdin.readline().split()))
ARC_List = list(map(int,sys.stdin.readline().split()))
    
HI_List.sort()
ARC_List.sort()
L = 0
M = 0
R = 0

for  i in range(HI):    
    a = bisect.bisect_left(ARC_List,HI_List[i])
    b = bisect.bisect_left(ARC_List,HI_List[i]+1)
    
    L += a
    M += b-a
    R += ARC - b
print(L,R,M)

