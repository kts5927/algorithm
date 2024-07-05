import sys

N, M = map(int, sys.stdin.readline().split())

def ccw(a, b, c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def snake(lst):
    cal = []
    cal.append(abs(lst[1][0] - lst[0][0] + lst[1][1] - lst[0][1]))

    for i in range(2, len(lst)):
        if ccw(lst[i-2], lst[i-1], lst[i]) < 0:
            cal.append('R')
        else:
            cal.append('L')
        cal.append(abs(lst[i][0] - lst[i-1][0] + lst[i][1] - lst[i-1][1]))
    return cal

def fail(a):
    l = len(a)
    cal = [0] * l
    j = 0
    for i in range(1, l):
        while j > 0 and a[i] != a[j]:
            j = cal[j-1]
        
        if a[i] == a[j]:
            j += 1
            cal[i] = j
        else:
            cal[i] = 0
    return cal

def kmp(a, b):
    
    start = b[0]
    end = b[-1]
    b = b[1:-1]
    cal = fail(b)
    l = len(b)
    ans = 0
    j = 0

    for i in range(len(a)):
        while j > 0 and a[i] != b[j]:
            j = cal[j-1]

        if a[i] == b[j]:
            if j == l - 1:
                if a[i-l] >= start and a[i+1]>=end:
                    ans += 1
                j = cal[j]
            else:
                j += 1
    return ans

def rev(lst: list):
    lst.reverse()
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] == 'R':
                lst[i] = 'L'
            else:
                lst[i] = 'R'
    return lst

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst2 = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

ans = 0
a = snake(lst)
b = snake(lst2)
d = rev(b.copy())
ans += kmp(a, b)

if b != d:
    ans += kmp(a, d)

print(ans)
