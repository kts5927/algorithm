N = int(input())
for i in range(N):
    lst = list(map(str,input().strip()))
    lst = [lst[0],lst[-1]]
    print(''.join(lst))