def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')
    tuple_list = [list(map(int, x.split(','))) for x in s]
    
    tuple_list = sorted(tuple_list, key=len)
    
    answer = []
    for t in tuple_list:
        for num in t:
            if num not in answer:
                answer.append(num)
    
    return answer

