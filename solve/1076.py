lst = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

ans = 0
for i in range(1,-1,-1):
    ans += lst.index(input())*10**i
print(ans * 10**lst.index(input()))
    