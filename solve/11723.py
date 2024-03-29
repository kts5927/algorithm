import sys

M = int(sys.stdin.readline())
S = []

for _ in range(M):
    string = list(map(str , sys.stdin.readline().split()))
    if len(string) == 2:
        a = string[0]
        b = string[1]
        
        if a == 'add' and 1 <= int(b) <= 20:
            S.append(int(b))
        elif a == 'remove' and int(b) in S and 1 <= int(b) <= 20:
            S.remove(int(b))
        elif a == 'check' and 1 <= int(b) <= 20:
            if int(b) in S:
                print(1)
            else :
                print(0)
        elif a == 'toggle' and 1 <= int(b) <= 20:
            if int(b) in S:
                S.remove(int(b))
            else:
                S.append(int(b))
    if string == 'empty':
        S = []
    elif string == 'all':
        S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]