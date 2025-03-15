n = int(input()) 
m = int(input())  

max_car = m  
current_car = m 

for _ in range(n):
    in_car, out_car = map(int, input().split())
    current_car += in_car - out_car 
    if current_car < 0: 
        print(0)
        break
    
    max_car = max(max_car, current_car)  

else:
    print(max_car)
