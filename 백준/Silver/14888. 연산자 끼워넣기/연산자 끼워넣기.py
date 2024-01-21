def calculate(a, b, n):
    if n == 0:  
        return a + b
    elif n == 1: 
        return a - b
    elif n == 2:  
        return a * b
    elif n == 3:  
        if a < 0:
            return -((-a) // b)
        else:
            return a // b

def function(idx, now, a, b):
    global max_, min_

    if idx == len(b) - 1: 
        max_ = max(max_, now)
        min_ = min(min_, now)
        return

    for i in range(4):
        if a[i] > 0:
            a[i] -= 1
            new_result = calculate(now, b[idx + 1], i)
            function(idx + 1, new_result, a, b)
            a[i] += 1

N = int(input())
arr = list(map(int, input().split()))
index = list(map(int, input().split()))

max_ = float('-inf')
min_ = float('inf')

function(0, arr[0], index, arr)

print(max_)
print(min_)
