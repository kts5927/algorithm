from collections import deque
N = int(input())

def cal(a,b,c):
    return a**2 + b**2 + c**2 + 7 * min(a, b, c)

ans = []
for i in range(N):
    a , b , c , d = map(int,input().split())
    while d>0:
        if d <10:
            deq = deque()
            deq.append([a,b,c,d])
            max_num = [0,0,0,0,0]
            while deq:
                A,B,C,D = deq.popleft()
                if max_num[4] < cal(A,B,C):
                    max_num = [A,B,C,D,cal(A,B,C)]
                if D > 0:
                    deq.append([A+1,B,C,D-1])
                    deq.append([A,B+1,C,D-1])
                    deq.append([A,B,C+1,D-1])
            a = max_num[0]
            b = max_num[1]
            c = max_num[2]
            d = max_num[3]
        else:
            if a >= b and a >= c:
                a += d
            elif b >= a and b >= c:
                b += d
            else:
                c += d
            d = 0
    ans.append(a**2 + b**2 + c**2 + 7 * min(a, b, c))

for i in ans:
    print(i)