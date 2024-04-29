import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = list(map(str,sys.stdin.readline().strip()))

count = 0
lenth = 0
ans = 0
while count < M:
    if S[count] == 'O':
        
        lenth = 0
    elif S[count] == 'I':
        if count+1 < M and S[count+1] == 'O' and count+2 < M and S[count+2] == 'I':
            if lenth == N-1:
               ans += 1
            else:
                lenth += 1

            count += 1
        else:
            lenth = 0
    count += 1        
print(ans)