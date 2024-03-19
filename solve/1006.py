import sys

def calculation():
    





T = int(sys.stdin.readline())

for k in range(T):
    N , W = map(int,sys.stdin.readline().split())
    ans = N*2
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    shadow = [[False for i in range(N)] for _ in range(2)]
    
    
    
    
    
    print('ans = ',ans)

# 6 10
# 9 2 2 7 5 4
# 4 2 10 1 2 7
# ans  = 7

# 5 6
# 3 1 2 4 2
# 5 6 1 3 2
# ans = 6