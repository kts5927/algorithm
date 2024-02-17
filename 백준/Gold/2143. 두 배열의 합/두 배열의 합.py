import sys
import bisect
T = int(sys.stdin.readline())
A_num = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B_num = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A_arr = []
B_arr = []
for i in range(A_num):
    pointer1 = i
    pointer2 = i
    while pointer2 != A_num:
        pointer2 += 1
        cal = A[pointer1:pointer2]
        A_arr.append(sum(cal))
        
for i in range(B_num):
    pointer1 = i
    pointer2 = i
    while pointer2 != B_num:
        pointer2 += 1
        cal = B[pointer1:pointer2]
        B_arr.append(sum(cal))
A_arr.sort()
B_arr.sort()
ans = 0
for i in range(len(A_arr)):
    number = T - A_arr[i]
    left = bisect.bisect_left(B_arr, number)
    right = bisect.bisect_right(B_arr, number)
    ans += (right - left)
print(ans)


