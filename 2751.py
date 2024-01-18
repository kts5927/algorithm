import sys
number = int(input())
list = []
for i in range(number):
    list.append(int(sys.stdin.readline()))

list.sort()
for i in list:
    print(i)