wood = list(map(int,input().split()))

while True:
    
    if wood == [1,2,3,4,5]:
        break
    for i in range(len(wood)-1):
        if wood[i] > wood[i+1]:
            wood[i],wood[i+1] = wood[i+1],wood[i]
            print(*wood)
