A, B = map(int, input().split()) 
arr = [0 for _ in range(60)]  
for i in range(1, 60):  
    arr[i] = 2**(i-1) + 2 * arr[i-1]  
    
def count(N):  
    count = 0  
    binary = bin(N)[2:]  
    length = len(binary)  
    for i in range(length):  
        if binary[i] == '1':  
            val = length-i-1  
            count += arr[val]  
            count += (N - 2**val + 1)  
            N = N - 2 ** val  
    return count  

print(count(B) - count(A-1))