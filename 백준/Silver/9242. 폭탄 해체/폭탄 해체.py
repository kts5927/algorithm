import sys

_0 = ['***','* *','* *','* *','***']
_1 = ['  *','  *','  *','  *','  *']
_2 = ['***','  *','***','*  ','***']
_3 = ['***','  *','***','  *','***']
_4  = ['* *','* *','***','  *','  *']
_5 = ['***','*  ','***','  *','***']
_6 = ['***','*  ','***','* *','***']
_7 = ['***','  *','  *','  *','  *']
_8 = ['***','* *','***','* *','***']
_9 = ['***','* *','***','  *','***']
numbers = [_0,_1,_2,_3,_4,_5,_6,_7,_8,_9]

lst = []

for i in range(5):
    lst.append(str(sys.stdin.readline()))
    
Len = len(lst[0])//4 
cal = ['','','','','']
ans = [-1]*Len

for i in range(Len):
    for j in range(5):
        cal[j] = "".join(lst[j][i*4:i*4+3])
    for k in range(10):
        if cal == numbers[k]:
            ans[i] = k
            break
    if ans[i] == -1:
        print("BOOM!!")
        exit() 
            

ans = int("".join(map(str, ans)))
if ans%6==0:
    print("BEER!!")
else:
    print("BOOM!!")