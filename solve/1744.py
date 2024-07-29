import sys

def cal(lst:list):
    
    n = 0
    while lst:
        if len(lst) > 1:
            if lst[-1]*lst[-2] > lst[-1]+lst[-2]:
                n += lst[-1]*lst[-2]
            else:
                n += (lst[-1] + lst[-2])
            
            lst.pop()
            lst.pop()
                
        else:
            n += lst[0]
            lst.pop()
    return n


N = int(sys.stdin.readline())
lst_up = []
lst_down = []

for i in range(N):
    a = int(sys.stdin.readline())
    if a > 0:
        lst_up.append(a)
    else:
        lst_down.append(a)
        
print(lst_up)
lst_up.sort()
lst_down.sort()
lst_down.reverse()

ans = 0
ans += cal(lst_up)
ans += cal(lst_down)
print(ans)
    
