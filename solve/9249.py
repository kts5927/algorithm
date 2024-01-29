A = input()
B = input()
text = A + '$' + B
n = len(text)

suffix = [i for i in range(n)]
g = [0]*(n+1)
ng = [0]*(n+1)

for i in range(n):
    g[i] = ord(text[i])

g[n] = -1
ng[suffix[0]] = 0
ng[n] = -1

t = 1
while t<n:
    
    suffix.sort(key = lambda x:(g[x],g[min(x+t,n)]))
    for i in range(1,n):
        p,q = suffix[i-1], suffix[i]
        if g[p] != g[q] or g[min(p+t,n)] != g[min(q+t,n)]:
            ng[q] = ng[p]+1
        else:
            ng[q] = ng[p]
            
    if ng[n-1] == n-1:
            break
    t = t*2
    g = ng[:]
    
LCP = [0]*n
length = 0
for i in range(n):
    k = g[i]
    if k == 0:
        continue
    p = suffix[k-1]
    
    while i+length < n and p + length < n and text[i+length] == text[p+length]:
        length +=1
    LCP[k] = length
    if length:
        length -= 1
        
    
m = (0,0)
for i , j in enumerate(LCP):
    if 0 <= suffix[i-1] + j - 1 < len(A) and len(A) < suffix[i] + j-1 < len(text):
        m = max(m,(j,i))
    if 0 <= suffix[i] + j - 1 < len(A) and len(A) < suffix [i-1] + j - 1 < len(text):
        m = max((m,(j,i)))


length, start = m
print(length)
print(text[suffix[start]: suffix[start] + length])