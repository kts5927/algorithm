T = int(input())  
results = []

for _ in range(T):
    V, E = map(int, input().split())  
    F = 2 - V + E 
    results.append(F)
for result in results:
    print(result)
