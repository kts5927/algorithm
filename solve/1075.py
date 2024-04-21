N = int(input())
F = int(input())

N = (N//100)*100

while True:
    
    if N%F == 0:
        break
    N += 1

a = list(map(str,str(N).strip()))


print(''.join(a[-2:]))