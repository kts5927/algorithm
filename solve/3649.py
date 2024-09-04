import sys

while True:
        
    try :
        N = int(sys.stdin.readline())
    except:
        break
    N *= 10000000
    A = int(sys.stdin.readline())
    lst = [0]*A
    for a in range(A):
        lst[a] = int(sys.stdin.readline())
        
    lst.sort()

    L = 0
    R = A-1

    ans = []
    while L < R:
        if lst[L] + lst[R] == N:
            ans.append([lst[L],lst[R]])
            L += 1
            
        elif lst[L] + lst[R] > N:
            R -=1
        elif lst[L] + lst[R] < N:
            L += 1

    cal = -1
    point = 0
    print(ans)
    for i in range(len(ans)):
        if abs(ans[i][0] - ans[i][1]) > cal:
            cal = abs(ans[i][0] - ans[i][1])
            point = i
    if cal == -1:
        print('danger')
    else:
        print('yes',ans[point][0],ans[point][1])