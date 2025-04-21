def sol():
    m = int(input())
    constellation = []
    for i in range(m):
        constellation.append(list(map(int, input().split())))

    stars = {}
    n = int(input())
    for i in range(n):
        X, Y = map(int, input().split())
        if X not in stars:
            stars[X] = set()
        stars[X].add(Y)

    for X, Y_list in stars.items():
        for Y in Y_list:
            move_X = constellation[0][0] - X
            move_Y = constellation[0][1] - Y 

            flag = 0
            for const in constellation:
                new_X = const[0] - move_X
                new_Y = const[1] - move_Y
                if new_X in stars and new_Y in stars[new_X]:
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                print(-move_X, -move_Y)
                exit() 
sol()