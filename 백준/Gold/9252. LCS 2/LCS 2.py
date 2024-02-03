import sys

first = list(str(sys.stdin.readline().strip()))
second = list(str(sys.stdin.readline().strip()))

LCS = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

i = len(first)
j = len(second)
lcs_length = LCS[i][j]
lcs_sequence = []

while lcs_length > 0:
    if first[i - 1] == second[j - 1]:
        lcs_sequence.append(first[i - 1])
        i -= 1
        j -= 1
        lcs_length -= 1
    elif LCS[i - 1][j] > LCS[i][j - 1]:
        i -= 1
    else:
        j -= 1

lcs_sequence.reverse()

print(len(lcs_sequence))
print(''.join(lcs_sequence))
