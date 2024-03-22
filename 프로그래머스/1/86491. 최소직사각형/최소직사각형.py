def solution(sizes):
    answer = 0
    first = 0
    second = 0
    
    for a , b in sizes:
        
        if a >= b:
            w = a
            h = b
        else : 
            w = b
            h = a
        
        if first == 0 and second == 0:
            first = w
            second = h
        
            
        if w > first:
            first = w
        
        if h > second :
            second = h
        
    return first * second