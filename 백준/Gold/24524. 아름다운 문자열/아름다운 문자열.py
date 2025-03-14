s = input()
t = input()

cnt = 0
l = [0 for _ in t] 
t_set = set(t)


for x in s:
    if x in t_set: 
        if x == t[0]: 
            l[0] += 1
        else:
            idx = t.find(x) 
            if l[idx - 1]:
                l[idx - 1] -= 1
                l[idx] += 1


print(l[-1])