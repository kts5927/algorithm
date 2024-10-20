import itertools

def find_next_larger_number(N):
    digits = list(range(1, 10))
    N_str = str(N)
    length = len(N_str)
    
    for perm in itertools.permutations(digits, length):
        num = int(''.join(map(str, perm)))
        if num > N:
            return num
    
    for perm in itertools.permutations(digits, length + 1):
        num = int(''.join(map(str, perm)))
        return num

while True:
    try:
        N = int(input().strip())
        result = find_next_larger_number(N)
        if result == None:
            result = 0
        print(result)
    except EOFError:
        break
