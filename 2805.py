a,b = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
d = 1 # 키 큰 나무들 중 몇번째를 자르고 있는가
t = 0 # 얼마나 잘랐는가
wood = 0 # 자른 나무의 길이는 총 얼마인가
totalcut = 0
if len(c) == 1 : 
    print(c[0]-b)
    exit()
while True: 
    if c[-d]-t > c[-d-1]:
        t+=1
        totalcut +=1
        wood += d
        
        if wood >= b : 
            print(c[-1]-totalcut)
            break
    else :
        d +=1 
        t = 0
        
    if d == len(c) :
        b -= wood
        e = b//len(c)
        if b%len(c) != 0:
            e +=1
        print(c[-1]-e - totalcut)
        
        
        break      

        
