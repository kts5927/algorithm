N = int(input())
cal = 0
for i in range(1,N+1):
    cal += i
print(cal)
print(cal**2)
cal = 0
for j in range(1,N+1):
    cal += j**3
print(cal)