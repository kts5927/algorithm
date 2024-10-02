def solution(clothes):
    answer = 1
    hash = {}
    for i in clothes:
        if i[1] in hash:
            hash[i[1]] += 1
        else:
            hash[i[1]] = 1
    print(hash)
    for i in hash:
        print(hash[i])
        answer *= hash[i]+1
        
    answer -= 1
    return answer