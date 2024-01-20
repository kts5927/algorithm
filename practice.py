def remove_from_left(matrix, column_index):
    for row in matrix:
        if row and len(row) > column_index:
            if isinstance(row[column_index], list) and len(row[column_index]) > 0:
                row[column_index].pop(0)
                if not row[column_index]:
                    row[column_index] = None

# 예시 2차원 배열 리스트
matrix = [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

# 1번째 열에서 왼쪽부터 하나씩 pop
remove_from_left(matrix, 0)

# 결과 확인
for row in matrix:
    print(row)
