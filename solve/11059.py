def find_longest_cree_string(s):
    n = len(s)
    prefix = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + int(s[i - 1])
    
    max_length = 0
    
    for length in range(2, n + 1, 2): 
        for start in range(n - length + 1):
            mid = start + length // 2
            end = start + length
            left_sum = prefix[mid] - prefix[start]
            right_sum = prefix[end] - prefix[mid]
            
            if left_sum == right_sum:
                max_length = max(max_length, length)
    
    return max_length

s = input().strip()
print(find_longest_cree_string(s))
