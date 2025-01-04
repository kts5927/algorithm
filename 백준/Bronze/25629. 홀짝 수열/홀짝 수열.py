def is_valid_holjjaksu_sequence(n, arr):
    odds = sorted([x for x in arr if x % 2 == 1])
    evens = sorted([x for x in arr if x % 2 == 0])

    if len(odds) + len(evens) != n:
        return 0

    hol_idx = 0
    jjk_idx = 0

    for i in range(n):
        if i % 2 == 0: 
            if hol_idx >= len(odds):
                return 0
            hol_idx += 1
        else:  
            if jjk_idx >= len(evens):
                return 0
            jjk_idx += 1

    return 1


n = int(input())
arr = list(map(int, input().split()))

print(is_valid_holjjaksu_sequence(n, arr))
