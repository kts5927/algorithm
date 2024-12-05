import sys
input = sys.stdin.readline

a , b = map(str,input().split())
A = list(map(int,a.strip()))
B = list(map(int,b.strip()))


       
print(sum(A)*sum(B)) 