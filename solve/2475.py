arr = list(map(int,input().split()))
sum_arr = 0

for i in arr:
    sum_arr += i**2
print(sum_arr%10)