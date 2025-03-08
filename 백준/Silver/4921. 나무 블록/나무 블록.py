next = [[], [4,5], [], [4,5], [2,3], [8], [2,3], [8], [6,7]]
num = 0

while True:
    N = int(input())
    if N == 0:
        break
    

    num += 1
    block = list(str(N).strip()) 
    if block[0] != '1':
        print(f"{num}. NOT")
        continue

    valid = True
    for i in range(len(block) - 1):
        if int(block[i+1]) not in next[int(block[i])]:
            print(f"{num}. NOT")
            valid = False
            break

    if valid and block[-1] != '2': 
        print(f"{num}. NOT")
    elif valid:
        print(f"{num}. VALID")
