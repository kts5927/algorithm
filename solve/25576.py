import sys
N,M = map(int,sys.stdin.readline().split())

ralpa = list(map(int,sys.stdin.readline().split()))
cal = [0 for _ in range(M)]

good = 0

for i in range(N-1):
    streamer = list(map(int,sys.stdin.readline().split()))
    for i in range(M):
        cal[i] = ralpa[i] - streamer[i]
    score = 0
    for i in cal:
        score += abs(i)
    
    if score <= 2000:
        good += 1
print(good)
if good >= (N-1)//2:
    print('NO')
else:
    print('YES')