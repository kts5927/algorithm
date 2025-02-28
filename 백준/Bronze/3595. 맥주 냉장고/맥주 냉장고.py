surface = float('inf')
n = int(input())


ans = [1,1,1]
Min = float('inf')
for a in range(1,int(n**0.5+1)):
    if n%a == 0:
        bc = n//a
        
        for b in range(1,int(bc**0.5+1)):
            if bc%b == 0:
                c = bc//b
                if a*b + b*c + c*a < Min:
                    Min = min(Min,a*b + b*c + c*a)
                    ans = [a,b,c]
print(*ans)
                