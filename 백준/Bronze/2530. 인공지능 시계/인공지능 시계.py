H, M, S = map(int,input().split())
time = int(input())

cal = H*60*60 + M*60 + S
cal += time

cal %= 60*60*24
lst = [0,0,0]
lst[0] = cal//60//60
lst[1] = cal//60%60
lst[2] = cal%60

print(*lst)