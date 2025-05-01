R, C = map(int, input().split())
parking_lot = [input().strip() for _ in range(R)]

result = [0] * 5

for i in range(R - 1):
    for j in range(C - 1):
        count = 0
        is_building = False
        for dx in range(2):
            for dy in range(2):
                ni, nj = i + dx, j + dy
                if parking_lot[ni][nj] == '#':
                    is_building = True
                elif parking_lot[ni][nj] == 'X':
                    count += 1
        if not is_building:
            result[count] += 1

for val in result:
    print(val)
