N, M = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()
print(lst[M-1])