import sys
N,K = map(int,sys.stdin.readline().split())
wallet = []
for i in range(N):
    coin = int(sys.stdin.readline())
    wallet.append(coin)
count=0
Teddy = K    
for i in reversed(wallet):
    if i <= Teddy:
        while i <= Teddy:    
            Teddy -= i
            count += 1
print(count)
            
        