import sys

def cal(string):
    n = len(string)
    fail = [0]*(n)
    j = 0

    for i in range(1, n):
        while j > 0 and string[i] != string[j]:
            j = fail[j - 1]

        if string[i] == string[j]:
            j += 1
            fail[i] = j

    return L - fail[-1]

L = int(sys.stdin.readline())
ad = str(sys.stdin.readline().rstrip())

print(cal(ad))