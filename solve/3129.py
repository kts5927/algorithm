import sys
before = list(map(str,sys.stdin.readline().strip()))
after = list(map(str,sys.stdin.readline().strip()))
before_len = len(before)
after_len = len(after)
ans = []
location = 0
for i in range(before_len - after_len+1):
    cal = []
    for j in range(after_len):
        a = ord(before[i+j]) - ord(after[j])
        if a < 0 :
            a += 26
        cal.append(a)
    for q in range(1,after_len//2+1):
        mini = cal[:q]
        for w in range(after_len):
            if cal[w] !=  mini[w%len(mini)]:
                break
            if w == after_len - 1:
                ans = mini
                location =  i
                cal = mini[len(mini) - location%len(mini):] + mini*(before_len // len(mini) + 1)
                real_ans = []
                for i in range(before_len):
                    a = ord(before[i]) - cal[i] - 97
                    if a < 0:
                        a += 26
                    real_ans.append(chr(a+97))
                print(''.join(real_ans))
                sys.exit()
