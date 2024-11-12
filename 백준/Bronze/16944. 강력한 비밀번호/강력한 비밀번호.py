N = int(input())
S = input().strip()

sep = [0 for _ in range(4)]
for char in S:
    if 'a' <= char <= 'z':
        sep[0] = 1  
    elif 'A' <= char <= 'Z':
        sep[1] = 1 
    elif '0' <= char <= '9':
        sep[2] = 1 
    elif char in "!@#$%^&*()-+":
        sep[3] = 1 

miss = 4 - sum(sep)

Min = max(0, 6 - N)

ans = max(miss, Min)

print(ans)
