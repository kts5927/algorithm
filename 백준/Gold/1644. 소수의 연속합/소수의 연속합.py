def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

N = int(input())
prime = []
for i in range(2, N + 1):
    if isPrime(i):
        prime.append(i)
ans = 0
start = 0
end = 0
while end <= len(prime):
    p_sum = sum(prime[start:end])
    if (p_sum == N):
        end += 1
        ans += 1
    if (p_sum < N):
        end += 1
    else : start += 1 
        
print(ans)