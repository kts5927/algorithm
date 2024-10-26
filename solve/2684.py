N = int(input())
for i in range(N):
    lst = list(map(str,input().strip()))
    
    count = [0 for _ in range(8)]
    
    for j in range(2,40):
        cal = 0
        if lst[j] == "H":
            cal += 1
        if lst[j-1] == "H":
            cal += 2
        if lst[j-2] == "H":
            cal += 4
        count[cal] += 1
    print()
    print(*count)