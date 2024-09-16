N = int(input())
A , B = 1,0

for i in range(N):
    A , B = B , A+B
print(A,B)