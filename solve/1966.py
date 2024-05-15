from collections import deque
T = int(input())

for i in range(T):
    N , M = map(int,input().split())
    lst = list(map(int,input().split()))
    cal = deque()
    for i in range(len(lst)):
        cal.append([lst[i],i])
    count = 0
    while len(lst) > 0:
        max_ = 0
        for i in range(1,len(cal)):
            if max_ <= cal[i][0]:
                max_ = cal[i][0]
        if cal[0][0] >= max_:
            a , b = cal.popleft()
            count+=1
            if b == M:
                break
        else:
            a , b = cal.popleft()
            cal.append([a,b])

    print(count)