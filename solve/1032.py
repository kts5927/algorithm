import sys

T = int(sys.stdin.readline())
text = [list(map(str,sys.stdin.readline().strip())) for _ in range(T)]
length = len(text[0])
ans = text[0]
for i in range(len(text)):
    for j in range(length):
        if ans[j] != text[i][j]:
            ans[j] = '?'
            
print(''.join(ans))