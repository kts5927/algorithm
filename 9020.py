import math
a = int(input())


for z in range(a):
    numbers = int(input())
    wanted = int(numbers/2)
    for x in range(0,wanted):
            count = 0
            for i in range(2,int(math.sqrt(wanted-x)+1)):
                if (wanted - x) % i == 0:
                    count+=1
                if count == 0:
                     for k in range(2,int(math.sqrt(wanted+x)+1)):   
                        if (wanted + x) % k == 0:
                            count+=1    
            if count == 0:
                print(wanted-x,wanted+x)
                break
 