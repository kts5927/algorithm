N = int(input())
fibo = [0,1,1] + [0 for _ in range(N-2)] 
for i in range(3,len(fibo)):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[N])