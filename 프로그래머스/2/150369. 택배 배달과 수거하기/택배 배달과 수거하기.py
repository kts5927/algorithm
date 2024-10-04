def makelst(lst: list, cap, n):
    ret = []
    box = cap
    location = -1
    i = 0
    while i < n: 
        if lst[i] != 0:
            if location == -1:
                location = i

            # lst[i]가 남은 box보다 적거나 같으면 모두 처리
            if box >= lst[i]:
                box -= lst[i]
                lst[i] = 0
            else:
                lst[i] -= box
                box = 0

            # 더 넣을 수 없으면/내릴 수 없으면 돌아가기
            if box == 0:
                ret.append(n - location)
                location = -1
                box = cap

        if lst[i] == 0:
            i += 1

    # 아직 남은 짐이 있으면 마지막 거리를 추가
    if location != -1:
        ret.append(n - location)
            
    return ret

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 계산 간편화를 위한 reverse
    deliveries.reverse()
    pickups.reverse()
    
    # 각 리스트에 대한 거리 계산
    lst1 = makelst(deliveries, cap, n)
    lst2 = makelst(pickups, cap, n)
    
    # 두 리스트의 길이를 맞추기 위한 패딩 추가
    max_len = max(len(lst1), len(lst2))
    lst1 += [0] * (max_len - len(lst1))
    lst2 += [0] * (max_len - len(lst2))
    
    # 최대값을 취해 총 이동 거리를 계산
    for i in range(max_len):
        answer += max(lst1[i], lst2[i])
        
    return answer * 2  # 왕복 거리 계산
