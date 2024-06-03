lst = [input().strip() for _ in range(8)]
count = 0
for i in range(8):
    for j in range(8):
        if lst[i][j] == 'F' and (i+j)%2 == 0:
            count += 1
            
print(count)