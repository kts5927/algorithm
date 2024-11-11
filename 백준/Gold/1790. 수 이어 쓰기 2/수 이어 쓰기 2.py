N, K = map(int, input().split())

count = 0
pointer = 1 
start = 1

while True:
    end = min(N, 10**pointer - 1)
    numbers_in_this_range = end - start + 1
    digits_in_this_range = numbers_in_this_range * pointer
    
    if count + digits_in_this_range >= K:
        break
    
    count += digits_in_this_range
    pointer += 1
    start *= 10
    
    if count < 0:
        print(-1)
        exit(0)

K -= count
target_number = start + (K - 1) // pointer
digit_position = (K - 1) % pointer

if target_number > N:
    print(-1)
else:
    print(str(target_number)[digit_position])
