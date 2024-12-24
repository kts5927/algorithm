def minimum_time_to_exercise(N, m, M, T, R):
    # 초기값 설정
    current = m
    total_time = 0
    exercise_time = 0

    # 맥박이 한 번도 운동을 시작할 수 없는 경우
    if m + T > M:
        return -1

    # 운동 목표 시간 충족될 때까지 반복
    while exercise_time < N:
        if current + T <= M:
            # 운동을 선택
            current += T
            exercise_time += 1
        else:
            # 휴식을 선택
            current = max(m, current - R)
        total_time += 1

    return total_time


# 사용자 입력 처리
if __name__ == "__main__":
    N, m, M, T, R = map(int, input().split())
    print(minimum_time_to_exercise(N, m, M, T, R))
