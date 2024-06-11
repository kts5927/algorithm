import sys
input = sys.stdin.read
data = input().split()

v = [[0, 0] for _ in range(90)]
n = int(data[0])
index = 1

for i in range(n):
    c = data[index]
    t = int(data[index + 1])
    index += 2
    v[ord(c)][t % 2] += 1  # 0 is even, 1 is odd

ans = 0
for b in range(2):
    for e in range(2):
        for s in range(2):
            for i in range(2):
                for g in range(2):
                    for o in range(2):
                        for m in range(2):
                            if ((b + e + s + s + i + e) * (g + o + e + s) * (m + o + o)) % 2 == 0:
                                ans += (v[ord('B')][b] * v[ord('E')][e] * v[ord('S')][s] *
                                        v[ord('I')][i] * v[ord('G')][g] * v[ord('O')][o] *
                                        v[ord('M')][m])
print(ans)
