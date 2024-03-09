point = ord("a")-1

N = int(input())
string = list(map(str , input().strip()))

count = 0
sum = 0
for i in string:
    sum += ((ord(i)-point) * 31**count)
    count+=1
    sum % 1234567891
print(sum)