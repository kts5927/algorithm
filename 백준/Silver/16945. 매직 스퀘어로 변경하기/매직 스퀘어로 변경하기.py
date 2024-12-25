

def check(lst):
    Sum = [0 for _ in range(8)]
    
    for i in range(3):
        Sum[i] = sum(lst[i])
    for i in range(3):
        for j in range(3):
            Sum[j+3] += lst[i][j]
    Sum[6] = lst[0][2] + lst[1][1] + lst[2][0]
    Sum[7] = lst[0][0] + lst[1][1] + lst[2][2]
    
    for i in Sum:
        if i != 15:
            return False
    return True
    

def cal(Magic:list,lst,i,j):
    global ans , use
    for k in range(1,10):
        if use[k] == False :
            use[k] = True
            lst[i][j] = k
            if i == 2 and j == 2:
                a = 0
                if check(lst):
                    A = 0 
                    for q in range(3):
                        for w in range(3):
                            A += abs(Magic[q][w] - lst[q][w])
                    ans = min(ans,A)
            else:
                if j == 2:
                    cal(Magic,lst,i+1,0)
                else:
                    cal(Magic,lst,i,j+1)
            use[k] = False
            lst[i][j] = 0
                         
    
    
    

Magic = [list(map(int,input().split())) for _ in range(3)]
lst = [[0 for _ in range(3)] for _ in range(3)]
use = [False for _ in range(10)]
ans = 999
cal(Magic,lst,0,0)
print(ans)