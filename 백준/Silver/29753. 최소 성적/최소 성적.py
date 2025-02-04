n, x = input().split()
n = int(n)
x = int(x[0] + x[2:])
s = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
t = [450, 400, 350, 300, 250, 200, 150, 100, 0]
u = dict(zip(s, t))
tot = 0
tos = 0
for i in range(n-1):
    a, b = input().split()
    a = int(a)
    b = u[b]
    tot += a
    tos += a * b
tou = int(input())
tot += tou
tov = x * tot
ans = 'impossible'
for i in u:
    # print(i, u[i], (tos + u[i] * tou) * 100 / tot // 100, tov * 100 / tot // 100)
    if (tos + u[i] * tou) * 100 / tot // 100 > tov * 100 / tot // 100:
        ans = i
print(ans)