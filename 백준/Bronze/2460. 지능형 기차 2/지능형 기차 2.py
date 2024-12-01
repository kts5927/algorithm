current_passengers = 0
max_passengers = 0

for _ in range(10):  
    off, on = map(int, input().split()) 
    current_passengers -= off
    current_passengers += on   
    max_passengers = max(max_passengers, current_passengers) 

print(max_passengers)
