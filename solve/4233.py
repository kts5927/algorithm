def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


while True:
    p, a = map(int, input().split())
    
    if a == 0 and p == 0:
        break
    
    cal = 1
    dup = a
    upper = p
    
    while True:
        if upper % 2 == 1:
            cal *= dup
            cal %= p
        
        upper = upper // 2
        if upper == 0:
            break
        dup = dup * dup
        dup %= p 
    
    print('p, a =', p, a)
    if cal % p == a:

        
        if not is_prime(p):
            print('yes')
        else:
            print('no')
    else:
        print('no')
