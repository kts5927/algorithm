A,B = map(str,input().split())


ans = 99
for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            count += 1
    ans = min(ans,count)
    
    
print(ans)