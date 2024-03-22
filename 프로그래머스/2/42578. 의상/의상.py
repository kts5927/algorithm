def solution(clothes):

    dic = {}
    for cloth , type_ in clothes:
        if type_ in dic.keys():
            dic[type_] += [cloth]
        else : 
            dic[type_] = [cloth]
            
    answer = 1
    for _ , lst in dic.items():
        answer *= (len(lst) + 1)
    
    return answer - 1