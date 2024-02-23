import sys
from collections import deque
string = deque(map(str,sys.stdin.readline().strip()))

sign = []
ans = []
while string:
    a = string.popleft()
    if(65 <= ord(a) <= 90):
        ans.append(a)
    else :
        if len(sign) == 0:
            sign.append(a)
        elif a == "*" or a == "/":
            if sign[-1] == "*" or sign[-1] == "/":
                ans.append(sign.pop())
                sign.append(a)
            else : sign.append(a)
        elif a == "+" or a == "-":
            if sign[-1] == "*" or sign[-1] == "/":
                while True:
                    if sign[-1] != "(":
                        ans.append(sign.pop())
                    else : break
                    if len(sign) == 0:
                        break
                sign.append(a)
            elif sign[-1] == "+" or sign[-1] == "-":
                ans.append(sign.pop())
                sign.append(a)    
            else:      
                sign.append(a)
        elif a == "(":
            sign.append(a)
        elif a == ")" :  
            while True:
                if sign[-1] == "(":
                    sign.pop()
                    break
                ans.append(sign.pop())
                
    if len(string) == 0:
        while True:
            if len(sign) > 0 :
                if sign[-1] != "(":
                    ans.append(sign.pop())
                else : sign.pop()
            if len(sign) == 0:
                break
print(*ans , sep='')