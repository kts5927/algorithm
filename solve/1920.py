a = int(input())
ali = set(map(int,input().split()))
b = int(input())
bli = list(map(int,input().split()))
for i in bli:
    if i in ali:
        print(1)        
    else :
        print(0)