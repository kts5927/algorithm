D,H,W = map(int,input().split())

pit = (H**2+W**2)**0.5/D
print(int(H/pit),int(W/pit))