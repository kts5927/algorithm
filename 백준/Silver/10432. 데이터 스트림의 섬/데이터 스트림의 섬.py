def sol():
    P = int(input())
    for _ in range(P):
        data = list(map(int, input().split()))
        T, a = data[0], data[1:]
        cnt = 0
        for l in range(1, 11):
            m = a[l]
            for r in range(l, 11):
                if a[r] < m:
                    m = a[r]
                if m > a[l - 1] and m > a[r + 1]:
                    cnt += 1
        print(T, cnt)

sol()