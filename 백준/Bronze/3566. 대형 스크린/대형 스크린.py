import math

bigMonitor = list(map(int, input().split(" ")))
T = int(input())

monitors = []
for i in range(T):
    monitors.append(list(map(int, input().split(" "))))

def returnDim(target, m):
    hNum = math.ceil(target[2] / m[2])
    vNum = math.ceil(target[3] / m[3])
    while hNum * m[0] < target[0]:
        hNum += 1
    while vNum * m[1] < target[1]:
        vNum += 1
    return [hNum, vNum, m[4] * hNum * vNum]

def returnCost(target, m):
    dim1 = returnDim(target, m)
    dim2 = returnDim(target, rotate(m))
    return min(dim1[2], dim2[2])

def rotate(m):
    return [m[1], m[0], m[3], m[2], m[4]]

costList = []
for m in monitors:
    costList.append(returnCost(bigMonitor, m))

print(min(costList))
