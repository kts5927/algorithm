A, B = input().split()

min_A = int(A.replace('6', '5'))
min_B = int(B.replace('6', '5'))
min_sum = min_A + min_B

max_A = int(A.replace('5', '6'))
max_B = int(B.replace('5', '6'))
max_sum = max_A + max_B

print(min_sum, max_sum)
