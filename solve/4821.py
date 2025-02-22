import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    pages = set() 
    page_input = input().split(',')

    for part in page_input:
        if '-' in part:
            s, e = map(int, part.split('-'))
            if s <= e:  
                for i in range(max(1, s), min(N, e) + 1): 
                    pages.add(i)
        else:
            num = int(part)
            if 1 <= num <= N: 
                pages.add(num)

    print(len(pages))
