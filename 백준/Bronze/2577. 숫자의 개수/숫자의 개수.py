A = int(input())
B = int(input())
C = int(input())

numbers = [0 for _ in range(10)]
number = A*B*C
while number > 0:
    numbers[number%10]+=1
    number //=10

for i in range(0,10):
    print(numbers[i])