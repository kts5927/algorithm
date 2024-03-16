import sys
import math

n = int(sys.stdin.readline())
solved = []
if n > 0 :
    for i in range(n):
        solved.append(int(sys.stdin.readline()))
    solved.sort()
    per = n * 0.15
    per = math.floor(per+0.5)
    ans = solved[per:len(solved)-per]
    cal = sum(ans)/len(ans)

    cal = math.floor(cal+0.5)
        
    print(cal)
else : print(0)