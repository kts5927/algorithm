T = int(input())
n = int(input())
candy = list(map(int,input().split()))
if sum(candy) < T:
    print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy")