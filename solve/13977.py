import sys

mod = 1000000007
fact = [1]*4000001

for i in range(2,4000001):
    fact[i] = (fact[i-1]*i)%mod
    
def power(n , a):
    
    result  = 1
    while a:
        if a%2 == 1:
            result *= n
        n *= n
        n = n%mod
        a = a//2
    
    return result

T = int(sys.stdin.readline())
for i in range(T):
    n,r = map(int,sys.stdin.readline().split())
    print((fact[n]*power(fact[n-r]*fact[r],mod-2))%mod)  