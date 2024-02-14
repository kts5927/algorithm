def cal(row, colum, square, sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if not (row[i] & (1 << k)) and not (colum[j] & (1 << k)) and not (square[i // 3 * 3 + j // 3] & (1 << k)):
                        row[i] |= (1 << k)
                        colum[j] |= (1 << k)
                        square[i // 3 * 3 + j // 3] |= (1 << k)
                        sudoku[i][j] = k

                        if cal(row, colum, square, sudoku):
                            return True

                        row[i] &= ~(1 << k)
                        colum[j] &= ~(1 << k)
                        square[i // 3 * 3 + j // 3] &= ~(1 << k)
                        sudoku[i][j] = 0
                return False
    return True

sudoku = [list(map(int, input().strip())) for _ in range(9)]

row = [0 for _ in range(10)]
colum = [0 for _ in range(10)]
square = [0 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            row[i] |= (1 << sudoku[i][j])
            colum[j] |= (1 << sudoku[i][j])
            square[i // 3 * 3 + j // 3] |= (1 << sudoku[i][j])

if cal(row, colum, square, sudoku):
    for row in sudoku:
        print(*row, sep='')
