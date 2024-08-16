
def cal(lst:list):
    start = 0
    ans = 0
    for i in lst:
        if i > start:
           ans += 1
           start = i
    return ans 


N = int(input())
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
    
    
print(cal(lst))
lst.reverse()
print(cal(lst))