N = int(input())
for j in range(N):
    lst = []
    for i in range(N):
        lst.append("@@@@@")
    print("".join(lst))
for k in range(3):
    for i in range(N):
        lst = []
        for j in range(N):
            lst.append("@")
        for j in range(N):
            lst.append("   ")
        for j in range(N):
            lst.append("@")
        print("".join(lst))
for j in range(N):
    lst = []
    for i in range(N):
        lst.append("@@@@@")
    print("".join(lst))
