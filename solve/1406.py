import sys
left = list(sys.stdin.readline().strip())
right = []

N = int(input())
for i in range(N):
    
    command = list(map(str,input().split()))
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop()) 
    elif command[0] == 'B':
        if left:
            left.pop() 
    elif command[0] == 'P':
        left.append(command[1])


right.reverse()

ans = left+right
print(''.join(ans))
    