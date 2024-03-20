import sys
while True:
    yelling = True
    arr = str(sys.stdin.readline())
    if arr == '.\n':
        break
    arr = list(map(str , arr.strip()))
    close = []
    for i in arr:
        if i == '(':
            close.append('(')
        elif i == '[':
            close.append('[')
        elif i == ')':
            if len(close) > 0 and close[-1] == '(':
                close.pop()
            else : 
                print('no')
                yelling = False
                break
        elif i == ']':
            if len(close) > 0 and close[-1] == '[':
                close.pop()
            else : 
                print('no')
                yelling = False
                break
       

        
    if len(close) == 0  and i != ')' and i != ']':
        print('yes')
    elif yelling:
        print('no')