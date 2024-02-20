import sys
sys.setrecursionlimit(10**6)

n = int(input())
i_o   = list(map(int,input().split()))
p_o   = list(map(int,input().split()))

table = [0] * (n+1)
for i in range(n):
    table[i_o[i]] = i

print(table)
def pre(i_s,i_e,p_s,p_e):
    if i_s > i_e  or p_s > p_e:
        return

    root = p_o[p_e]

    left = table[root] - i_s
    right = i_e - table[root]
    
    print(root, end = " ")
    pre(i_s,i_s+left-1,p_s,p_s+left-1)
    pre(i_e-right+1,i_e,p_e-right,p_e-1)

pre(0,n-1,0,n-1)