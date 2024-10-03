def solution(fees, records):
    
    # fees : 기본시간, 기본요금, 단위시간, 단위요금
    # records : 시각(시:분), 차량번호, 내역
    answer = []
    
    Limit = 23 * 60 + 59  # 하루 끝 시간을 분으로 환산
    parking_times = {}  # 차량별 총 주차 시간을 기록할 딕셔너리
    in_times = {}  # 차량별 입차 시간을 기록할 딕셔너리

    # 모든 입차, 출차 기록 처리
    for record in records:
        time, car_number, action = record.split()
        hour, minute = map(int, time.split(':'))
        current_time = hour * 60 + minute  # 시간을 분으로 변환
        
        if action == "IN":
            in_times[car_number] = current_time  # 입차 시간 기록
        elif action == "OUT":
            parking_time = current_time - in_times.pop(car_number)  # 출차 시간 - 입차 시간
            if car_number in parking_times:
                parking_times[car_number] += parking_time  # 누적 주차 시간 갱신
            else:
                parking_times[car_number] = parking_time  # 첫 기록일 경우

    # 출차 기록 없는 차량 처리 (23:59 출차로 간주)
    for car_number, in_time in in_times.items():
        parking_time = Limit - in_time
        if car_number in parking_times:
            parking_times[car_number] += parking_time
        else:
            parking_times[car_number] = parking_time

    # 요금 계산
    for car_number in sorted(parking_times.keys()):
        total_time = parking_times[car_number]
        if total_time <= fees[0]:  # 기본시간 이하
            answer.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_fee = (extra_time + fees[2] - 1) // fees[2] * fees[3]
            answer.append(fees[1] + extra_fee)

    return answer
