import bisect
from sys import stdin

def find_shark(T, shark):
    cal = bisect.bisect_left(shark, T)
    return cal

N, K, T = map(int, stdin.readline().split())
shark = list(map(int, stdin.readline().split()))

shark.sort()

count = 0

for i in range(K):
    position = find_shark(T, shark)
    
    if position > 0:
        T += shark[position - 1] 
        count += 1
        del shark[position - 1] 
    else:
        break  

print(T)
