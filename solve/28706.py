# import sys
# input = sys.stdin.readline

# T = int(input())
# for i in range(T):
#     case = []
#     N = int(input())
#     for j in range(N):
#         case.append(list(map(str,input().split())))
    
#     DP = [0 for k in range(2**(N+1))]
#     DP[0] = 1
#     for q in range(1,N+1):
#         for w in range((2**q)-1,2**(q+1)-1):
#             if w%2 == 1:
#                 cal = (w+1)//2-1
#                 if case[q-1][0] == '+':
#                     DP[w] = DP[cal] + int(case[q-1][1])
#                 else:
#                     DP[w] = DP[cal] * int(case[q-1][1])
#             elif w%2 == 0:
#                 cal = w//2-1
#                 if case[q-1][2] == '+':
#                     DP[w] = DP[cal] + int(case[q-1][3])
#                 else:
#                     DP[w] = DP[cal] * int(case[q-1][3])
#     ans = 'UNLUCKY'
#     for i in range(len(DP)//2-1,len(DP)-1):
#         if DP[i]%7 == 0:
#             ans = 'LUCKY'
#             break
#         print('i = ',i)
#     print('ans = ', ans)
    
import sys

input = sys.stdin.readline

def calculate(command, dp_set):
    temp = set()
    for i in range(0, 4, 2):
        oper, num = command[i], command[i+1]
        for operand in dp_set:
            if oper == "+":
                temp.add((operand + int(num)) % 7)
            else:
                temp.add((operand * int(num)) % 7)
    return temp

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        commands = [list(map(str, input().split())) for _ in range(N)]
        dp_set = set([1]) # 1부터 시작
        for command in commands:
            dp_set = calculate(command, dp_set)
            
        if 0 in dp_set:
            print("LUCKY")
        else:
            print("UNLUCKY")