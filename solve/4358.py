import sys
dic = {}
for i in range(10000000):
    n = sys.stdin.readline().rstrip()
    if n == "":
        break
    elif n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

dic_len = sum(dic.values())
arr = sorted(dic.keys())

for i in arr:
    if i == "": break
    num = (dic[i] / dic_len) * 100
    print(i, format(num, '.4f'))