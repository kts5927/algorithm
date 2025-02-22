T = int(input())
for i in range(T):
    n = int(input())
    ans = []
    for i in range(n//5):
        ans.append('+++++')
    cal = []
    for i in range(n - (n//5)*5):
        cal.append('|')
    ans.append(''.join(cal))
    print(' '.join(ans))