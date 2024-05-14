import bisect

def find_lis(sequence):
    lis = []
    lis_indices = []
    for i in range(len(sequence)):
        pos = bisect.bisect_left(lis, sequence[i])
        if pos == len(lis):
            lis.append(sequence[i])
        else:
            lis[pos] = sequence[i]
        lis_indices.append((pos, sequence[i], i))
    lis_length = len(lis)
    lis_result = []
    for pos, value, idx in reversed(lis_indices):
        if pos == lis_length - 1:
            lis_result.append(idx)
            lis_length -= 1
    lis_result.reverse()
    return lis_result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    wires = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(n)]
    
    wires.sort()
    
    positions = [b for a, b in wires]
    
    lis_indices = find_lis(positions)
    
    lis_set = set(lis_indices)
    
    result = []
    for i in range(n):
        if i not in lis_set:
            result.append(wires[i][0])
    
    result.sort()
    
    print(len(result))
    for num in result:
        print(num)

if __name__ == "__main__":
    main()
