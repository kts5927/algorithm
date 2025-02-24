cow = list(map(str,input().strip()))
ans = 0
for start in range(len(cow)):
    for end in range(start+1,len(cow)):
        if cow[start] == cow[end]:
            cal = cow[start:end+1]
            for k in cal:
                if cal.count(k) == 1:
                    ans += 1
            break
print(ans//2)