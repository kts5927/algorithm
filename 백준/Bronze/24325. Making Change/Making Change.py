def calculate_change(n, data_sets):
    results = []
    denominations = [50, 20, 10, 5, 1] 
    
    for cost, payment in data_sets:
        change = round((payment - cost) * 100)  
        
        counts = []
        for denom in denominations:
            denom_cents = denom * 100 
            count = change // denom_cents
            counts.append(count)
            change %= denom_cents
        
        results.append(f"{counts[0]}-$50, {counts[1]}-$20, {counts[2]}-$10, {counts[3]}-$5, {counts[4]}-$1")
    
    return results

n = int(input()) 
data_sets = []

for _ in range(n):
    cost, payment = map(float, input().split())
    data_sets.append((cost, payment))

output = calculate_change(n, data_sets)

for line in output:
    print(line)
