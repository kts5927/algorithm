import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    Case = []
    for j in range(N):
        Case.append(list(map(int,input().split())))
    Case.sort()
    
    D,S,E = 0,0,0
    count = 0
    for d,s,e in Case:
        if D != d:
            D = d
            S = s
            E = e
            count += 1
        else:
            if E > s and E > e:
                S = s
                E = e
            elif E <= s:
                S = s
                E = e
                count += 1
                
        
        
    print('Scenario #', i+1, ':', sep='')
    print(count)
    print()