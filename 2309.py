a = []
for i in range(9):
    a.append(int(input()))
ghost = sum(a) - 100    

catch = False
for i in range(9):
    for j in range(i+1,9):
        if a[i] + a[j] == ghost : 
            del a[i] , a[j-1]
            catch = True
            break
        
    if catch :
        break
a.sort()
for i in range(len(a)) : 
    print(a[i])