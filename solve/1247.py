for i in range(3):
    N = int(input())
    ans = 0
    for j in range(N):
        ans += int(input())
    if ans > 0:
        print('+')
    elif ans == 0:
        print(0)
    else:
        print('-')