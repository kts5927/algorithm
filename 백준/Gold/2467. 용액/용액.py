import sys
N = int(sys.stdin.readline())
liq = list(map(int,sys.stdin.readline().split()))
left = 0
right = N-1

ans_sum = float('inf')
ans_location = []

while left != right:
    if abs(liq[left] + liq[right]) <= abs(ans_sum):
        ans_sum = liq[left] + liq[right]
        ans_location = [liq[left] , liq[right]]
        if abs(liq[left]) >= abs(liq[right]):
            left += 1
        elif abs(liq[left]) < abs(liq[right]):
            right -= 1
    elif abs(liq[left] + liq[right]) > abs(ans_sum):
        if abs(liq[left]) > abs(liq[right]):
            left += 1
        elif abs(liq[left]) < abs(liq[right]):
            right -= 1
        
print(*ans_location)