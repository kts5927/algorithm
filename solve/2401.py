import sys

def calculate(words, String, N, L):
    canPaste = {}

    for i in range(N):
        s = words[i]
        l = len(s)
        if l > L:
            continue
        
        fail = [0] * l
        j = 0
        for k in range(1, l):
            while j > 0 and s[k] != s[j]:
                j = fail[j-1]
            if s[k] == s[j]:
                j += 1
                fail[k] = j

        j = 0
        for k in range(L):
            while j > 0 and String[k] != s[j]:
                j = fail[j-1]
            if String[k] == s[j]:
                if j == l - 1:
                    if k-l+1 not in canPaste:
                        canPaste[k-l+1] = []
                    canPaste[k-l+1].append(l)
                    j = fail[j]
                else:
                    j += 1
    
    return canPaste


def solve(String, canPaste, L):
    cache = [0] * (L + 1)

    for pos in range(L - 1, -1, -1):
        cache[pos] = cache[pos + 1]
        if pos in canPaste:
            for word_length in canPaste[pos]:
                cache[pos] = max(cache[pos], cache[pos + word_length] + word_length)
    
    return cache[0]


String = sys.stdin.readline().strip()
L = len(String)
N = int(sys.stdin.readline().strip())

words = [sys.stdin.readline().strip() for _ in range(N)]

canPaste = calculate(words, String, N, L)
result = solve(String, canPaste, L)
print(result)
