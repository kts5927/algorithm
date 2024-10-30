N = int(input())
Str1 = list(map(str, input().strip()))
lst1 = [0] * 26  

for char in Str1:
    lst1[ord(char) - ord('A')] += 1

count = 0  

for _ in range(N - 1):
    Str2 = list(map(str, input().strip()))
    lst2 = [0] * 26  

    for char in Str2:
        lst2[ord(char) - ord('A')] += 1

    diff_count = 0  
    for i in range(26):
        diff_count += abs(lst1[i] - lst2[i])

    if diff_count == 0: 
        count += 1
    elif diff_count == 1: 
        count += 1
    elif diff_count == 2 and len(Str1) == len(Str2):  
        count += 1

print(count)