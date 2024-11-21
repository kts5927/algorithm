def count_squares(n):
    return sum((n - k + 1) ** 2 for k in range(1, n + 1))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    results = []
    for line in data:
        n = int(line)
        if n == 0:
            break
        results.append(count_squares(n))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
