P = int(input())
for _ in range(P):
    inputs = input().split()
    N = int(inputs[0])
    D = float(inputs[1])
    A = float(inputs[2])
    B = float(inputs[3])
    F = float(inputs[4])
    
    collision_time = D / (A + B)
    fly_distance = F * collision_time
    
    print(f"{N} {fly_distance:.6f}")
