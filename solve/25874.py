import math

def find_divisors(n):
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_power_of_ten(x):
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5
    return x == 1

def main():
    N = int(input().strip())
    
    # 1. N의 약수 구하기
    divisors = find_divisors(N)
    
    # 2. 10의 거듭제곱이 될 수 있는 X 찾기
    valid_x = []
    for d in divisors:
        if is_power_of_ten(d):
            valid_x.append(d)
    
    # 3. 결과 출력
    print(len(valid_x))
    for x in sorted(valid_x):
        print(x)

if __name__ == "__main__":
    main()
