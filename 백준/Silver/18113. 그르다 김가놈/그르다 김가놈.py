import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

def count_pieces(P):
    total = 0
    for L in lengths:
        if L <= K:
            continue
        if L < 2*K:

            remain = L - K
        else:
            remain = L - 2*K
        
        if remain <= 0:
            continue
        
        total += remain // P
        if total >= M:
            break
    return total

left, right = 1, max(lengths)  
answer = -1
while left <= right:
    mid = (left + right) // 2
    if count_pieces(mid) >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
