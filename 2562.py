numbers = []
count = 0

for i in range(0,9):
    numbers.append(int(input()))    
for a in range(0,8):
    
    if numbers[a]>numbers[a+1]:
        count = count + 1
        numbers[a+1] = numbers[a]
    else: 
        count = 0
        
print(*numbers[8:9])
print(9 - count)
