import sys
N = int(input())
line = []
temp = []
number = []
def binary(left , right , a , x):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    return left

for i in range(N):
    line.append(list(map(int,sys.stdin.readline().split())))

line.sort(key= lambda x:x[0])
location = [line[0][1]]
number = [-1]*N
for i in range(N):
    if location[-1] < line[i][1]:
        number[i] = max(number) + 1
        location.append(line[i][1])
    else:        
        x = binary(0,len(location) - 1, location, line[i][1]) #왼쪽에서 나옴
        if line[i][1] > location[x]:
            location[-1] = line[i][1] # LIS에 추가되어도 된다고 판단시 교체
            
        else :
            location[x] = line[i][1]
            number[i] = x+1 # number의 길이는 관리되고 있음으로 number의 index = LIS 길이    

print(N-len(location))
r = len(location)
cal = []
for i in range(N-1 , -1 , -1):
    if r == 0:
        break
    if number[i] == r:
        cal.append(line[i])
        r -= 1
        
ans = []
for i in line:
    if i not in cal:
        ans.append(i)
        
ans.sort(key = lambda x:x[0])
for i in range(N-len(location)):
    print(ans[i][0])