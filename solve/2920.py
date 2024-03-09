arr = list(map(int,input().split()))

ascending = True
descending = True

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        descending = False
    if arr[i] < arr[i-1]:
        ascending = False
        
if ascending:
    print('ascending')
elif descending:
    print('descending')
else : print('mixed')