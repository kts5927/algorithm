A, B = map(int, input().split())
result = 0
pos = 1
num = 1

while pos <= B:
    cnt = 0
    while cnt < num and pos <= B:
        if pos >= A:
            result += num
        pos += 1
        cnt += 1
    num += 1

print(result)
