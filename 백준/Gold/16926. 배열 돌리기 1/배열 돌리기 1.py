def rotate_layer(matrix, layer, N, M):
    top = layer
    left = layer
    bottom = N - 1 - layer
    right = M - 1 - layer

    top_left = matrix[top][left]
    
    for i in range(left, right):
        matrix[top][i] = matrix[top][i + 1]
    
    for i in range(top, bottom):
        matrix[i][right] = matrix[i + 1][right]
    
    for i in range(right, left, -1):
        matrix[bottom][i] = matrix[bottom][i - 1]
    
    for i in range(bottom, top, -1):
        matrix[i][left] = matrix[i - 1][left]
    
    matrix[top + 1][left] = top_left

def rotate_counterclockwise(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    N = len(matrix)
    M = len(matrix[0])
    
    layers = min(N, M) // 2
    
    for layer in range(layers):
        rotate_layer(matrix, layer, N, M)
    
    return matrix

N , M , R= map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

for i in range(R):
    matrix = rotate_counterclockwise(matrix)

for row in matrix:
    print(*row)
