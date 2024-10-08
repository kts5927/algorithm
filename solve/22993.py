import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
player = lst[0]
enemy = lst[1:]
enemy.sort()
for i in enemy:
    if player > i:
        player += i
    elif player <= i:
        print('No')
        exit()
print('Yes')