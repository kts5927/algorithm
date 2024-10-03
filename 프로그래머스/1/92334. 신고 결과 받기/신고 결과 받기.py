def solution(id_list, report, k):
    id_len = len(id_list)
    answer = [0]*id_len
    
    index = {}
    for i in range(id_len):
        index[id_list[i]] = i 
        
    cal = [[] for _ in range(id_len)]
    for i in report:
        a,b = map(str,i.split())
        if a not in cal[index[b]]:
            cal[index[b]].append(a)
    
    for i in cal:
        if len(i) >= k:
            for j in i:
                answer[index[j]] += 1
    return answer