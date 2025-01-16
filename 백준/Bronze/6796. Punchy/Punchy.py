A, B = 0, 0

while True:
    command = input().split()  
    instruction = int(command[0])  

    if instruction == 1: 
        X, n = command[1], int(command[2])
        if X == 'A':
            A = n
        else:
            B = n
    elif instruction == 2: 
        X = command[1]
        if X == 'A':
            print(A)
        else:
            print(B)
    elif instruction == 3: 
        X, Y = command[1], command[2]
        if X == 'A':
            A += A if Y == 'A' else B
        else:
            B += A if Y == 'A' else B
    elif instruction == 4:  
        X, Y = command[1], command[2]
        if X == 'A':
            A *= A if Y == 'A' else B
        else:
            B *= A if Y == 'A' else B
    elif instruction == 5:  
        X, Y = command[1], command[2]
        if X == 'A':
            A -= A if Y == 'A' else B
        else:
            B -= A if Y == 'A' else B
    elif instruction == 6:  
        X, Y = command[1], command[2]
        if X == 'A':
            A //= A if Y == 'A' else B
        else:
            B //= A if Y == 'A' else B
    elif instruction == 7: 
        break