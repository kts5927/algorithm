import sys

# lst = [0,1,3,7]
# for i in range(10):
#     lst.append(lst[-1]+lst[-2]+lst[-3]+3)
#  배열을 구하는 식

N = int(sys.stdin.readline())
lst = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
for i in range(N):
    a = int(sys.stdin.readline())
    print(lst[a])