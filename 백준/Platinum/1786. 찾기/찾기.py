import sys
T = list(map(str,sys.stdin.readline().rstrip('\n')))
P = list(map(str,sys.stdin.readline().rstrip('\n')))
def kmp(arr:list , compare:list):
    table = [0 for _ in range(len(compare))]
    i = 0
    for j in range(1,len(compare)):
        while i>0 and compare[i] != compare[j]:
            i = table[i-1]
            
        if compare[i] == compare[j]:
            i += 1
            table[j] = i
            
    result = []
    i = 0
    for j in range(len(arr)):
        while i>0 and compare[i] != arr[j]:
            i = table[i-1]
            
        if compare[i] == arr[j]:
            i += 1
            if i == len(compare):
                result.append(j-i+2)
                i = table[i-1]
                
    return result
print(len(kmp(T,P)))        
print(*kmp(T,P))