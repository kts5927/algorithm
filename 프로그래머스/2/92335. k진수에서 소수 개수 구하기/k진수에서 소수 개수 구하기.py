def solution(n, k):
    # 소수 리스트 생성 (에라토스테네스의 체)
    limit = 100000
    prime = [True] * (limit + 1)
    prime[0], prime[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    
    # 진수 변환
    change = []
    while n >= k:
        change.append(n % k)
        n //= k
    change.append(n)
    change.reverse()

    # 변환된 숫자들을 문자열로 합쳐서 0으로 분리
    change_str = ''.join(map(str, change))
    split_nums = change_str.split('0')  # 0을 기준으로 분리
    
    answer = 0
    
    for num_str in split_nums:
        if num_str.isdigit() and num_str != '':  # 빈 문자열이 아닌 경우만 처리
            num = int(num_str)
            if num > 1 and (num <= limit and prime[num] or num > limit and is_prime(num)):
                answer += 1

    return answer

# 큰 수에 대한 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
