T = int(input())
for i in range(T):
    load = list(map(int,input().split()))
    load.sort()
    print((load[0]+load[1])**2 + load[2]**2)