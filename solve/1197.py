import sys
V,E = map(int,sys.stdin.readline().split())
lists = []
parents = [None] * (V+1)
for i in range(1,V+1):
    parents[i] = i

for i in range(E):
    parent,child,cost = map(int,sys.stdin.readline().split()) 
    lists.append([cost,parent,child])
    
lists.sort()
cost = 0
for i in range(E):
    if parents[lists[i][1]] != parents[lists[i][2]] : 
        cost += lists[i][0]
        a1 = parents[lists[i][1]]
        a2 = parents[lists[i][2]]
        
        for j in range(1,V+1):
            if parents[j] == a2:
                parents[j] = a1
print(cost)