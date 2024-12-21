mod = 1000000007

def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def matrix_exponentiation(base, exp):
    n = len(base)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # 단위 행렬
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exp //= 2
    return result

def dp_with_matrix(n, a, b, c):
    initial = [[a], [b], [c]]
    
    transform = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    
    transform_n = matrix_exponentiation(transform, n)
    
    result = matrix_multiply(transform_n, initial)
    return result

n = int(input())
a, b, c = 1, 1, 1
result = dp_with_matrix(n-1, a, b, c)
ans = sum(i[0] for i in result) % mod
print(ans)