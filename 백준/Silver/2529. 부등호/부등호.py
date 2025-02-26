def backtrack(location:int, cal:list):
    global Max,Min
    if location == K:
        if int(Max) < int(''.join(map(str,cal))):
            Max = ''.join(map(str,cal))
        if int(Min) > int(''.join(map(str,cal))):
            Min = ''.join(map(str,cal))

        return
    
    for i in range(10):
        if number[i] == False:
            if sign[location] == '<' and cal[-1] < i or sign[location] == '>' and cal[-1] > i:
                cal.append(i)
                number[i] = True
                backtrack(location+1, cal)
                cal.pop()
                number[i] = False
                

K = int(input())
sign = list(map(str,input().split()))
number = [False for _ in range(10)]
cal = []
Max = -9999999999
Min = 9999999999
for i in range(10):
    
    cal.append(i)
    number[i] = True
    
    backtrack(0,cal)
    
    cal.pop()
    number[i] = False
print(Max)
print(Min)