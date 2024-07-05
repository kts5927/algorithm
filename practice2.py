import sys

N , M = map(int,sys.stdin.readline().split())

def Rotation(lst , num):
    cal = []
    if num == 0:    
        for i in lst:
            cal.append([-i[1],i[0]])
    elif num == 1:
        for i in lst:
            cal.append([-i[0],-i[1]])
    elif num == 2:
        for i in lst:
            cal.append([i[1],-i[0]])
    else:
        return lst
    return cal


def lst_rev(cal:list):
    cal.reverse()
    cal = [[-1 * x for x in row] for row in cal]
    return cal

def fail(p):
    m, j = len(p), 0
    pi = [0]*m
    for i in range(1, m):
        while j > 0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j+=1
            pi[i] = j
    return pi

def check(word,pattern,kmp):
    table = fail(pattern)
    results = 0
    pat_len = len(pattern)
    j = 0
   
    flag = False
    for i in range(kmp,kmp+pat_len):
        if flag:
            return 0
        if j == 0 or j == pat_len-1:
            if word[i]*pattern[j] >= 0 and abs(word[i]) >= abs(pattern[j]):
                if j == len(pattern)-1:
                    results+=1
                    j = table[j]
                else:
                    j += 1
        else:
            if word[i] != pattern[j]:
                flag = True
            j += 1
    # print(word , pattern , results)
    return results

def match_conditions(text_vector, pattern_vector, is_first, is_last):
    if is_first or is_last:
        return (text_vector[0] * pattern_vector[0] >= 0 and abs(text_vector[0]) >= abs(pattern_vector[0])) and \
               (text_vector[1] * pattern_vector[1] >= 0 and abs(text_vector[1]) >= abs(pattern_vector[1]))
    else:
        return text_vector == pattern_vector

def KMP(pattern):
    table = fail(pattern)
    results = 0
    pat_len = len(pattern)
    j = 0
    
    for i in range(N - M+2):

        if j == 0 or j == pat_len-1:
            if word[i][0]*pattern[j][0] >= 0 and abs(word[i][0]) >= abs(pattern[j][0]) and word[i][1]*pattern[j][1] >= 0 and abs(word[i][1]) >= abs(pattern[j][1]):
                if j == pat_len-1:
                    results += 1
                    j = table[j]
                else:
                    j += 1
            else:
                j = table[j-1]
        else:
            while j > 0 and word[i] != pattern[j] :
                j = table[j-1]
            if word[i] == pattern[j]:
                j += 1
    # print(word , pattern , results)
    return results

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lst2 = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
word = []
ans = 0
for i in range(1,len(lst)):
    word.append([lst[i][0]-lst[i-1][0] , lst[i][1]-lst[i-1][1]])
len_word = len(word)    

cal2 = []
for i in range(1,len(lst2)):
    cal2.append([lst2[i][0]-lst2[i-1][0] , lst2[i][1]-lst2[i-1][1]])

for i in range(4):
    cal = 0
    snake =  Rotation(cal2,i)
    cal = KMP(snake)
    ans += cal

    snake = lst_rev(snake)
    ans += KMP(snake)
print(ans)


