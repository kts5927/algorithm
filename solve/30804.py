import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    Tanghulu = list(map(int,input().split()))

    L = -1
    R = -1
    fruit = [0 for _ in range(10)]
    num = 0
    ans = 0
    while R < N-1:

        if fruit.count(0) < 8:
            L += 1
            fruit[Tanghulu[L]] -= 1
            num -= 1

        else:
            R += 1
            num += 1
            fruit[Tanghulu[R]] += 1
            
        if fruit.count(0) >= 8:
            ans = max(ans,num)
            

            
    print(ans)
sol()