que = []
number,put = map(int,input().split())
ans = []
for i in range(number):
    que.append(i+1)
    
while True:
    for i in range(put-1):
        que.append(que[0])
        que.pop(0)
    ans.append(que[0])
    que.pop(0)
    if len(que) == 0:
        break
print('<',end = "")
for i in range(len(ans)-1):
    print(ans[i], end=", ")
print(ans[number-1],end="")
print('>')
