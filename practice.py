from collections import deque
a = deque()
a.append([1,2])
print(a)
b = a[0][0]
c = a[0][1]
print(b,c)
a.append([1,2])
print(a)
d = a[1][0]
e = a[1][1]

print(d,e)
a.popleft()
a.popleft()
print(a)
a.append([1,2])

print(a)