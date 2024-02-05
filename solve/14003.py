import sys

A = int(input())
arr = list(map(int,sys.stdin.readline().split()))

duplicant = [arr[0]]
replica = [(0,arr[0])]



def binarysearch(n):
    start = 0
    end = len(duplicant)-1
    while start <= end:
        mid = (start+end)//2
        if duplicant[mid] == n:
            return mid
        elif duplicant[mid] < n:
            start = mid+1
        else:
            end = mid - 1
    return start

for i in range(1,A):
    if arr[i] > duplicant[-1]:
        duplicant.append(arr[i])
        replica.append((len(duplicant)-1,arr[i]))
    else:
        idx = binarysearch(arr[i])
        duplicant[idx] = arr[i]
        replica.append((idx,arr[i]))
        
print(len(duplicant))

last_idx = len(duplicant)-1
ans = []
print(duplicant)
for i in range(len(replica)-1,-1,-1):
    if replica[i][0] == last_idx:
        ans.append(replica[i][1])
        last_idx -= 1
        
print(*ans[::-1])