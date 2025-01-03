import sys
input = sys.stdin.readline

N , M = map(int,input().split())
A = list(map(int,input().split()))

Start,End,Sum,ans = 0,0,0,0
while End < len(A):

    Sum += A[End]
    while Sum > M and Start <= End:
        Sum -= A[Start]
        Start += 1
    ans = max(ans,Sum)
    End += 1    
print(ans)