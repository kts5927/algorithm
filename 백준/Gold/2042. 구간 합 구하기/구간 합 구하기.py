import sys
N, M, K = map(int,sys.stdin.readline().split())

l = []
seg = [0]*(N*4)

def init(start, end, i):
    if start == end:
        seg[i] = l[start-1]
        return seg[i]
	
    mid = (start+end) // 2
    seg[i] = init(start, mid, i*2) + init(mid+1, end, i*2+1)
    return seg[i]

       
def find(start, end, i, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return seg[i]

    mid = (start + end) // 2
    cal = find(start, mid, i*2, left, right) + find(mid+1, end, i*2+1, left, right)
    return cal


def update(start, end, i, update_idx, update_data):
    if start > update_idx or end < update_idx:
        return
    
    seg[i] += update_data
	
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, i*2, update_idx, update_data)
    update(mid+1, end, i*2+1, update_idx, update_data)

for _ in range(N):
    l.append(int(sys.stdin.readline()))

init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,sys.stdin.readline().split())
    if a == 1:
        temp = c - l[b-1]
        l[b-1] = c
        update(1, N, 1, b, temp)

    elif a == 2:
        print(find(1, N, 1, b, c))