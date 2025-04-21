import sys
input = sys.stdin.readline

def sol():
    T = int(input())
    for i in range(T):
        wood, ant = map(int,input().split())
        Max, Min = -float('inf'),-float('inf')
        for j in range(ant):
            location = int(input())
            Max = max(max(location, wood-location),Max)
            Min = max(min(location, wood-location),Min)
            
        print(Min,Max)
sol()