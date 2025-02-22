import sys
input = sys.stdin.readline

rate = {
    'F': 0,
    'D0': 100,
    'D+': 150,
    'C0': 200,
    'C+': 250,
    'B0': 300,
    'B+': 350,
    'A0': 400,
    'A+': 450
}

N,score = input().split()
score = int(score[0]+score[2:])
lst = []
class_num = 0
for i in range(int(N)-1):
    lst.append(list(map(str,input().split())))
    class_num += int(lst[-1][0])
n = int(input())
class_num += n
cal = 0
for num, credit in lst:
    cal += (int(num)*rate[credit])


ans = 'impossible'
for credit,num in rate.items():
    if (cal + n*num)*100/class_num//100 > score:
        ans = credit
        break
print(ans)