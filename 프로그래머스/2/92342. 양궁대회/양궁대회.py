def solution(n, info):
    answer = []
    
    lst = [[0]*11 for _ in range(4096)]
    
    
    for i in range(1,4097):
        if (i//2048)%2 == 1:
            lst[i][0] = info[0]+1
        if (i//1024)%2 == 1:
            lst[i][1] = info[1]+1
        if (i//512)%2 == 1:
            lst[i][2] = info[2]+1
        if (i//256)%2 == 1:
            lst[i][3] = info[3]+1
        if (i//128)%2 == 1:
            lst[i][4] = info[4]+1
        if (i//64)%2 == 1:
            lst[i][5] = info[5]+1
        if (i//32)%2 == 1:
            lst[i][6] = info[6]+1
        if (i//16)%2 == 1:
            lst[i][7] = info[7]+1 
        if (i//8)%2 == 1:
            lst[i][8] = info[8]+1
        if (i//4)%2 == 1:
            lst[i][9] = info[9]+1
        if (i//2)%2 == 1:
            lst[i][10] = info[10]+1
            

    
    cal = []
    for i in lst:
        if sum(i) <= n:
            cal.append(i)
            
    ans = []
    score = 0
    for i in cal:
        me = 0
        enemy = 0
        for j in range(11):
            
            if i[j] > info[j]:
                me += (10-j)
            elif i[j] <= info[j] and info[j] > 0:
                enemy += (10-j)
                
        if score <= me-enemy:
            if score < me-enemy:
                ans = []
            if me - enemy > 0:
                i[10] += (n-sum(i))
                i.reverse()
                ans.append(i)
            score = me-enemy
            
    ans.sort()
    for i in ans:
        print(i)
    if len(ans) > 0:
        a = ans[-1]
        a.reverse()
        answer = a
    else:
        answer = [-1]
    return answer