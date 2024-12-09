N = input()

p = 0
num = 0

while True:
    num += 1
    
    for i in str(num):
        if N[p] == i:
            p += 1
            if p >= len(str(N)):
                print(num)
                exit()