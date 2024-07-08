import sys

N = int(sys.stdin.readline())
lst = list(map(str,sys.stdin.readline().rstrip()))

start = 0
end = 0

tp = [0]*26
tp[ord(lst[start])-ord('a')] += 1
count = 1
ans = 1

while start != len(lst)-2:
    while tp.count(0) >= 26-N and end < len(lst)-1:
        end += 1
        tp[ord(lst[end]) - ord('a')] += 1
        count += 1

    if tp.count(0) >= 26-N:
        ans = max(count , ans)
        break
    else:
        ans = max(count-1 , ans)
    while tp.count(0) < 26-N and start < end:
        tp[ord(lst[start]) - ord('a')] -= 1
        start += 1
        count -= 1

print(ans)