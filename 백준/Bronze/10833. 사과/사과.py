T = int(input())
ans = 0
for i in range(T):
    student,apple = map(int,input().split())
    ans += apple%student
    
print(ans)