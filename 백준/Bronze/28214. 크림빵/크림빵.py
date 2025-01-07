N, K, P = map(int, input().split())
cream_bread = list(map(int, input().split()))

sellable_bundles = 0

for i in range(N):
    bundle = cream_bread[i * K:(i + 1) * K]  
    no_cream_count = bundle.count(0) 
    if no_cream_count < P:
        sellable_bundles += 1

print(sellable_bundles)
