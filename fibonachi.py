#a = int(input())
#f1 = 0
#f2 = 1
#f3 = 1
#for i in range(a-2):
#   f1 = f2 + f3
#   f3 = f2
#   f2 = f1 
   
#if a == 1:
#    f1 = 1
#if a == 2:
#    f1 =1
#print(f1)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else : return fibo(n-1) + fibo(n-2)
    
n = int(input())
print(fibo(n))