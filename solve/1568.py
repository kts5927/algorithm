N = int(input())
a = 1
count = 0
while N > 0:
    if N - a >=0:
        N -= a
        a += 1
        count += 1
    else:
        a = 1
print(count)