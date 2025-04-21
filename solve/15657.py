import sys
input = sys.stdin.readline

def dfs(lst:list, ans:list, depth:int,  Len:int):
    for i in range(Len):
        if  ans[-1] <= lst[i]:
            if len(ans) < depth:
                ans.append(lst[i])
                dfs(lst,ans,depth,Len)
                ans.pop()
            else:
                print(*ans)
                return
        
    return

def sol():
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    Len = len(lst)
    for i in range(Len):
        dfs(lst,[lst[i]],M,Len)
sol()