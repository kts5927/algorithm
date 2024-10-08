# import time

# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#     	return fibo(n-1) + fibo(n-2)
# start_time = time.time()

# # 실행할 코드
# print(fibo(40))

# end_time = time.time()
# print(f"실행 시간: {end_time - start_time}초")


def solution(n, k):
    answer = 0
    
    
    # 소수 만들어서 hash로 저장
    prime = [i for i in range(10000)]
    for i in range(2,10000):
        for j in range(2,10000//i):
            if prime[i*j] != 0:
                
                prime[i*j] = 0
                
    prime = set(prime)
    prime.remove(0)
    prime.remove(1)
    
    # 진수 변환
    change = []
    while n > k:
        change.append(n%k)
        n //= k
    change.append(n)
    change.reverse()
    
    
    #계산
    cal = []
    change.append(0)
    for i in change:
        if i != 0:
            cal.append(str(i))   
        else:
            num = int(''.join(cal))
            if num in prime:
                answer += 1
            cal = []
    return answer

print(solution(110011, 10))