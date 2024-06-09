import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    N, K = map(int, data[0].split())
    
    gratitude_count = defaultdict(int)
    last_occurrence = {}
    
    for i in range(1, 3 * N + 1):
        gratitude = data[i]
        gratitude_count[gratitude] += 1
        last_occurrence[gratitude] = i
    
    sorted_gratitudes = sorted(gratitude_count.keys(), key=lambda x: (-gratitude_count[x], -last_occurrence[x]))
    
    for gratitude in sorted_gratitudes[:K]:
        print(gratitude)

if __name__ == "__main__":
    main()
