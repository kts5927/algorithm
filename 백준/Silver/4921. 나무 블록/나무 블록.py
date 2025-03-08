import sys
input = sys.stdin.readline
next = {
    1: {4, 5},
    2: {},
    3: {4, 5},
    4: {2, 3},
    5: {8},
    6: {2, 3},
    7: {8},
    8: {6, 7}
}
num = 0
while True:
    N = int(input())
    if N == 0:
        break

    
    num += 1
    
    block = list(str(N).strip())
    if block[0] != '1' or block[-1] != '2':
        print(f'{num}.','NOT')
        continue
    vn = 'VALID'
    for i in range(len(block)-1):
        if int(block[i+1]) not in next[int(block[i])]:
            vn = 'NOT'
            break
    print(f'{num}.',vn)