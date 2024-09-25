N = int(input())
lst = list(map(str,input().strip()))
compare = ['g','o','r','i']
point = 0
for i in lst:
    if i == compare[point]:
        point += 1
    else:
        point = 0
    if point == 4:
        print('YES')
        break
if point != 4:
    print('NO')