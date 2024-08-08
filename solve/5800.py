N = int(input())
for i in range(N):
    lst = list(map(int,input().split()))
    print(f"Class {i+1}")
    l = lst[1:]
    l.sort()
    a = 0
    for i in range(1,len(l)):
        if l[i]-l[i-1] > a:
            a = l[i]-l[i-1]
    print(f"Max {l[-1]}, Min {l[0]}, Largest gap {a}")
