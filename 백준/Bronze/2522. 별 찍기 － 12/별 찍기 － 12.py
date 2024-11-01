N = int(input())

star = []
for i in range(1,N+1):
    lst = []
    for k in range(N-i):
        lst.append(' ')
    for k in range(i):
        lst.append('*')
    star.append(''.join(lst))
    
for i in range(N):
    print(star[i])
for i in range(2,N+1):
    print(star[N - i])