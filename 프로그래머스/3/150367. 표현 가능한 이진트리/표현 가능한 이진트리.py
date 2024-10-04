def DFS(lst):
    # 리스트 길이가 1일 경우 무조건 True
    if len(lst) == 1:
        return True
    
    # 가운데 노드 선택 (중간 위치)
    mid = len(lst) // 2
    
    # 가운데 노드가 0인데 서브트리에 1이 있으면 False
    if lst[mid] == 0 and (1 in lst[:mid] or 1 in lst[mid+1:]):
        return False
    
    # 왼쪽과 오른쪽 서브트리 각각 DFS로 탐색
    return DFS(lst[:mid]) and DFS(lst[mid+1:])

def TtoT(i):
    # 숫자를 이진수로 변환하고 리스트로 반환
    binary = []
    while i > 0:
        binary.append(i % 2)
        i //= 2
    binary.reverse()
    return binary

def pad_to_full_tree(binary):
    # 이진수를 2^n - 1 길이로 패딩
    length = len(binary)
    # 트리의 높이 n을 계산하여 필요한 노드 수 (2^n - 1) 구하기
    full_length = 1
    while full_length < length:
        full_length = full_length * 2 + 1
    
    # 부족한 부분을 0으로 채우기
    return [0] * (full_length - length) + binary

def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = TtoT(number)
        padded_binary = pad_to_full_tree(binary)
        
        if DFS(padded_binary):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
