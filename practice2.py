n = int(input())

g = n

for _ in range(n):
    s = input()
    a = [100]*26
    for i in range(len(s)):
        if a[ord(s[i])-97]==100: 
            a[ord(s[i])-97] = i
            
        else: 
            if i-a[ord(s[i])-97] > 1: 
                g -= 1
                break
            else:
                a[ord(s[i])-97] = i
    
print(g)