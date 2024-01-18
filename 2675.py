a = int(input())

for i in range(a):
    number,text = input().split()
    
    for a in text:
        print(a*int(number),end = '')
        
    print()


##number,text = input().split을 썼을때 타입에러가 뜬다
