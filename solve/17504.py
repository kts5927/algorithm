N = int(input())
lst = list(map(int,input().split()))


a = 1
b = lst.pop()
c = lst.pop()

while lst:
    a_ = b
    b_ = b*c+a
    c_ = lst.pop()
    a = a_
    b = b_
    c = c_
    

print(b*c+a - b , b*c+a)   

    
