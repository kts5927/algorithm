A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0
was_winning = False

for i in range(9):
    A_score += A[i]
    if A_score > B_score:
        was_winning = True
    B_score += B[i]

print("Yes" if was_winning and B_score > A_score else "No")
