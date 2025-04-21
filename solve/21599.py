import sys
input = sys.stdin.readline
def sol():  
    T = int(input())
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)

    power = 0
    ans = 0
    for i in range(T):
        power = max(lst[i],power)
        if power == 0:
            break
        ans += 1
        power -= 1
        
    print(ans)
sol()