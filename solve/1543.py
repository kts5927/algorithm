import sys
lecture = list(map(str,sys.stdin.readline().strip()))
string = list(map(str,sys.stdin.readline().strip()))

location = 0
ans = 0

while location <= len(lecture) - len(string):
    match = True
    for i in range(len(string)):
        if lecture[location + i] != string[i]:
            match = False
            break
    if match:
        ans += 1
        location += len(string)
    else:
        location += 1

print(ans)
