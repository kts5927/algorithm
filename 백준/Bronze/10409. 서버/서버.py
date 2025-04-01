n,t = map(int,input().split())
server = list(map(int,input().split()))
for i in range(len(server)):
    t -= server[i]
    if t < 0:
        print(i)
        break
    
    if i == len(server)-1:
        print(i+1)