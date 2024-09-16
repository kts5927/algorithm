N = int(input())
AB = [1,0]

for i in range(N):
    calA = AB[0]
    calB = AB[1]
    AB[0] = calB
    AB[1] = calA + calB
print(AB)