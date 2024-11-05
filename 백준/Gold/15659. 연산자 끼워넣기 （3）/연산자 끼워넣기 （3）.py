import sys
input = sys.stdin.readline

def cal(a):
    global Max,Min
    Cal = [a[0]]
    for i in range(len(a)):
        if i > 0 and i%2 == 0:
            if a[i-1] == 2:
                Cal[-1] *= a[i]
            elif a[i-1] == 3:
                Cal[-1] = int(Cal[-1]//a[i])
            else:
                Cal.append(a[i-1])
                Cal.append(a[i])

    ans = Cal[0]
    for i in range(len(Cal)):
        if i>0 and i%2 == 0:
            if Cal[i-1] == 0:
                ans += Cal[i]
            else:
                ans -= Cal[i]


    Max = max(ans,Max)
    Min = min(ans,Min)

def Make(a,pointer):
    a[pointer] = numbers[pointer//2]
    pointer += 1
    if pointer == len(a):
        cal(a)
    
    for i in range(4):
        if sign[i] != 0:
            a[pointer] = i
            sign[i] -= 1
            Make(a,pointer+1)
            a[pointer] = 0
            sign[i] += 1

N = int(input())
numbers = list(map(int,input().split()))
sign = list(map(int,input().split()))
sign_sum = sum(sign)
Sign = [0 for _ in range(2*N-1)]
Max = -float('inf')
Min = float('inf')
Make(Sign,0)

print(Max)
print(Min)