import sys

def left(index,cal_1,cal_2,value):
    if value >=  cal_2[-1][0]:
        cal_2[-1][0] += cal_1[index][0]
        cal_2[-1][1] = cal_1[index][1]
    else:
        cal_2.append(cal_1[index])

def right(index,cal_1,cal_2,value):
    if value >= cal_1[index+1][0]:
        cal_2[-1][0] += cal_1[index+1][0]
        return index +1
    else:
        return index



T = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

microbe = []
for i in range(len(lst)):
    microbe.append([lst[i],i+1])

cal_1 = microbe
cal_2 = []
while len(cal_1) > 1 :
    length = len(cal_1)-1
    index = 0
    while index < len(cal_1):
        value = cal_1[index][0]
        if len(cal_2) == 0:
            cal_2.append(cal_1[index])
            index = right(index,cal_1,cal_2,value)

        else:    
            left(index,cal_1,cal_2,value)
            if index < length:
                index = right(index,cal_1,cal_2,value)

        index += 1

    cal_1 = cal_2
    cal_2 = []

for i in cal_1:
    for j in i:
        print(j)

