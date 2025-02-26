N = int(input())


for i in range(N):

    blink = [' ' for _ in range(N-i-1)]
    star = ['*' for _ in range(2*i+1)]
    cal = blink + star
    print(''.join(cal))
