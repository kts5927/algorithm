import sys

N , M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

total = 0
for i in lst:
    total += i

left = 0
right = total

while True:
    mid = (left + right) // 2
    cal = 0
    count = 0
    for i in lst:
        if cal > mid:
            cal = 0
            count += 1
        cal += i
    
    if count > M:
        right = mid
    