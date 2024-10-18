T = int(input())

for i in range(T):
    W , N = map(int,input().split())
    trash = []
    for j in range(N):
        x,w = map(int,input().split())
        trash.append([x,w])
       
    ans = 0
    cal = W 
    for x,w in trash:
        while w > 0:
            if cal == 0:
                cal = W
            
            if cal - w < 0:
                ans += x
                cal = 0
            else:
                cal -= w
                if cal == 0:
                    ans += x
                w = 0
    if cal != 0:
        ans += x
    print(ans*2)