import sys
input = sys.stdin.read

def solve():
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    items = list(enumerate(A))
    items.sort(key=lambda x: -x[1])

    used = [0] * N  
    placed = [0] * N  

    for i in range(N):
        placed[i] = items[i][0]

    strengthened = set()
    for i in range(N):
        idx = placed[i]
        power = A[idx]
        for j in range(power):
            pos = (i + j) % N
            strengthened.add(pos)

    print(len(strengthened))

solve()
