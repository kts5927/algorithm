lst = list(map(str,input().strip()))
left = lst[:len(lst)//2]
right = lst[(len(lst)+1)//2:]
right.reverse()
if left == right:
    print(1)
else:
    print(0)