String = []
for i in range(4):
    
    string = list(map(str,input().strip()))
    for i in range(len(string)):
        string[i] = ord(string[i])
    String.append(string)
    
    
string = list(map(str,input().strip()))
for i in range(len(string)):
    string[i] = ord(string[i])

cal = []
for i in range(len(string)):
    for j in range(4):
        for k in range(len(String[j])):
            if string[i] == String[j][k]:
                cal.append([j,k])
cal.sort()

print(chr(String[cal[4][0]][cal[4][1]]))