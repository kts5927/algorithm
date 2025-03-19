T = int(input())
name = [0 for _ in range(26)]
for i in range(T):
    player = list(map(str,input().strip()))
    name[ord(player[0])-ord('a')] += 1
    
ans = []
for i in range(26):
    if name[i] >= 5:
        ans.append(chr(i + ord('a')))
if ans == []:
    print("PREDAJA")
else:
    print(''.join(ans))