score = [0,':',0]
N = int(input())
for i in range(N):
    a = str(input())
    if a == 'D':
        score[0] += 1
    else:
        score[2] += 1
    if abs(score[0] - score[2]) == 2:
        break
score[0] = str(score[0])
score[2] = str(score[2])
print(''.join(score))