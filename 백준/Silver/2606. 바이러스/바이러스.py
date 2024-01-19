import sys
V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
lists = []
computer = [None] * (V+1)
computer[1] = True
for i in range(E):
    parent,child = map(int,sys.stdin.readline().split()) 
    lists.append([parent,child])
lists.sort()

def search(computer:list,lists:list,i:int):
    
    if computer[lists[i][0]] != computer[lists[i][1]]:
        computer[lists[i][1]] = True
        computer[lists[i][0]] = True
        for j in range(len(lists)):
            if lists[j][0] == lists[i][1]:
                search(computer, lists, j)
            elif lists[j][1] == lists[i][1]:
                search(computer, lists, j)
            elif lists[j][0] == lists[i][0]:
                search(computer, lists, j)
            elif lists[j][1] == lists[i][0]:
                search(computer, lists, j)
                   
for i in range(E):         
    search(computer,lists,i)

print(computer.count(True)-1)
