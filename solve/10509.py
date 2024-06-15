import sys

table  = [[0],
          [1,2,3,4,5,6,7,8,9,0],
          [2,3,5,6,8,9,0],
          [3,6,9],
          [4,5,6,7,8,9,0],
          [5,6,8,9,0],
          [6,9],
          [7,8,9,0],
          [8,9,0],
          [9]]

lst = []
T = int(sys.stdin.readline())
for k in range(200):
    number = list(map(int,str(k)))
    cal = []
    for i in number:
        if cal:
            if i not in table[int(cal[-1])]:
                min_ = 10000
                for j in table[int(cal[-1])]:
                    if abs(j-i) < abs(min_-i):
                        min_ = j
                    else:
                        min_ = min_
                cal.append(str(min_))
            else:cal.append(str(i))
        else:
            cal.append(str(i))
    num = int(''.join(cal))
    if num not in lst:
        lst.append(num)
length = len(lst)
ans = []
for i in range(T):
    number = int(sys.stdin.readline())
    min_ = 10000
    for j in range(length):
        if abs(number - lst[j]) <= abs(min_ - number):
            min_ = lst[j]
    ans.append(min_)

for i in ans:
    print(i)