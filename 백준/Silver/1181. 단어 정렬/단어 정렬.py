a = int(input())
b = [None]*a
for i in range(a):
    b[i] = input()
b = list(set(b))
b.sort()
b.sort(key = len)
for i in range(len(b)):
    print(b[i])