import sys
N , M , Q = map(int,sys.stdin.readline().split())
product = []
customer = []

raw = [0]
p_sum = [0] * (N+1)



for _ in range(N):
    product.append(list(map(int,sys.stdin.readline().split())))
    raw.append(product[-1][0])
    
for i in range(1 , N+1):
    p_sum[i] = p_sum[i-1] + raw[i]        
    
    
for _ in range(Q):
    day , start , end = map(int,sys.stdin.readline().split())
    ans = p_sum[end]-p_sum[start-1]

    for i in product[start-1 : end]:
        if i[1] == day:
            ans -= i[0]//2
    print(ans)