import sys
a , b = map(int,sys.stdin.readline().split())
k , x = map(int,sys.stdin.readline().split())
count = 0
for i in range(k-x,k+x+1):
    if i>=a and b>=i:
        count+=1
if count == 0:
    print('IMOPOSSIBLE')
else:
    print(count)