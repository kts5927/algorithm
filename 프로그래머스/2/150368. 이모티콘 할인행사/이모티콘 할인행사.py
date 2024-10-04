def solution(users, emoticons):
    answer = []
    
    discount = [10,20,30,40]
    lst = [[0] * len(emoticons) for _ in range(2**(2*len(emoticons)))]
    
    
    # 쿠폰 할인율 리스트
    for i in range(len(lst)):
        for j in range(len(emoticons)):
            lst[i][j] = discount[(i // 2**(j*2)) % 4]
            
        
    
    cal = []
    for discount_component in lst:
        sub = 0
        sell = 0
        for buy, wallet in users:
            money = 0 
                
            for w in range(len(emoticons)):
                if discount_component[w] >= buy:
                    money += (emoticons[w] * (100 - discount_component[w]) * 0.01)
                
            # print(discount_component, buy, money, wallet)
            if money >= wallet:
                sub += 1
            else:
                sell += money
                
        cal.append([sub, sell])

    cal.sort()
            
            
    answer = cal[-1]
    return answer