for i in range(3):
    a = list(map(int,input().split()))
    b = sum(a)
    if b == 0:
        print("D")
    elif b == 1:
        print("C")
    elif b == 2:
        print("B")
    elif b == 3:
        print("A")
    elif b == 4:
        print("E")