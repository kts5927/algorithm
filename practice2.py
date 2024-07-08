A, B, V = map(int, input().split())

cf=False
d=0

V1 = V - A
if(V1 < A):
    d = 1
else:
    d = V1//(A-B)
    temp = V1%(A-B)+A
    if(temp >= A):
        cf=True
    while(cf):
        if(temp >= A):
            temp -= A
            d+=1
        else:
            if(temp != 0):
                d+=1
            d-=1
            cf = False
        
print(d+1)