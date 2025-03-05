N = int(input())
tower = list(map(int,input().split()))

now = 0
pull = 0
for height in tower:
    if height >= now:
        pull += 1
    now = height
print(pull)