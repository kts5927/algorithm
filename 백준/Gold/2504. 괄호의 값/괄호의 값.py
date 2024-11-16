def Exit():
    print(0)
    exit()

def Append(a):
    LR.append(a)
    if a == '(':
        num[len(LR)].append(2)
    else:
        num[len(LR)].append(3)

def Pop(a):
    if LR and ((a == ')' and LR[-1] == '(') or (a == ']' and LR[-1] == '[')):
        if len(num) > len(LR) + 1 and num[len(LR) + 1]:
            num[len(LR)][-1] *= sum(num[len(LR) + 1])
            num[len(LR) + 1] = []
        LR.pop()
    else:
        Exit()

lst = list(input().strip())
LR = []
num = [[] for _ in range(len(lst) + 2)] 

for i in lst:
    if i in '([':
        Append(i)
    elif i in ')]':
        Pop(i)

if not LR:
    print(sum(num[1]))
else:
    Exit()
