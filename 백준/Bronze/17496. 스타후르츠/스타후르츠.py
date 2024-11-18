def calculate_earnings(N: int, T: int, C: int, P: int) -> int:
    harvest_days = (N - 1) // T 
    total_earnings = harvest_days * C * P
    return total_earnings

N, T, C, P = map(int, input().split())

print(calculate_earnings(N, T, C, P))
