import sys
input = sys.stdin.readline
def f(s):
    d = {
		'1': {'4','5'},'2': {},'3': {'4','5'},'4': {'2','3'},'5': {'8'},'6': {'2','3'},'7': {'8'},'8': {'6','7'}}
    if s[0] != '1' or s[-1] != '2':
        return 'NOT'
    for i in range(0, len(s) - 1):
        if s[i+1] not in d[s[i]]:
            return 'NOT'
    return 'VALID'
i = 0
while True:
    s = list(input().rstrip())
    if s == ['0']:
        break
    i += 1
    print(f'{i}.',f(s))