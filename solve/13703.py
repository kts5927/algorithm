import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr      = [0 for _ in range(k+n+1)]
temp = [0 for _ in range(k+n+1)]

arr[k] = temp[k] = 1

for i in range(n): 
    print(temp)
    for j in range(1, k+n+1):
        if arr[j]:
            temp[j-1] += temp[j] 
            temp[j+1] += temp[j]
            temp[j] = 0

    arr = temp[:] 
print(temp)
print(sum(arr)-arr[0])