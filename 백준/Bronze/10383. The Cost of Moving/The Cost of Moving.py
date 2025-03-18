import sys

def calculate_movement_cost(products):
    sorted_products = sorted(products)
    total_cost = 0
    
    for i, product in enumerate(products):
        sorted_index = sorted_products.index(product)
        total_cost += abs(i - sorted_index)
    
    return total_cost

def main():
    site_number = 1
    
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        
        products = []
        while len(products) < n:
            products.extend(sys.stdin.readline().strip().split())
        
        total_cost = calculate_movement_cost(products)
        print(f"Site {site_number}: {total_cost}")
        site_number += 1

if __name__ == "__main__":
    main()