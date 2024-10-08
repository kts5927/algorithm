A = [0]*30
A[0] = 1
A[1] = 1
A[2] = 5

B = [0]*30
B[1] = 1
B[2] = 1
C = [0]*30
C[1] = 1
C[2] = 2

for n in range(2,30):
    A[n]=A[n-2]+A[n-1]+B[n-1]+2*C[n-1]
    B[n]=B[n-2]+A[n-1]
    C[n]=C[n-1]+A[n-1]

T = int(input())
for i in range(T):
    N = int(input())
    print(A[N])
    
