import sys
N = int(sys.stdin.readline())
stack = []
cal = [0]
ans = []
tf = True
num = 1
for i in range(N):
    stack.append(int(sys.stdin.readline()))
    while True:
        if stack[0] > cal[-1]:
            ans.append('+')
            cal.append(num)
            num += 1
        elif stack[0] == cal[-1]:
            cal.pop()
            stack.pop()
            ans.append('-')
            break
        else : 
            print('NO')
            exit()
for i in ans:
    print(*i , end = '\n')

   
    
# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1