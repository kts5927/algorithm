import sys 

N = int(sys.stdin.readline().strip())
doll = list(map(int,sys.stdin.readline().split()))
cost = [0] * (max(doll)+1)

for i in doll:
    cost[i] += 1

result = 0
for i in range(max(doll),0,-1):
    while cost[i] != 0:
        count = 0
        while cost[i-count] != 0:
            cost[i-count] -= 1
            result += i
            count += 1

print(result)