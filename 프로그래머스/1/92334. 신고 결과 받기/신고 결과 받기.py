def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    index = {}
    for i in range(len(id_list)):
        index[id_list[i]] = i 
        
    cal = [[] for _ in range(len(id_list))]
    for i in report:
        a,b = map(str,i.split())
        if a not in cal[index[b]]:
            cal[index[b]].append(a)
    
    for i in cal:
        if len(i) >= k:
            for j in i:
                answer[index[j]] += 1
    return answer