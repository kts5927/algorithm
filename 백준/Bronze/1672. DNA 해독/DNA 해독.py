Table = \
[['A','G','C','T']
,['A','C','A','G']
,['C','G','T','A']
,['A','T','C','G']
,['G','A','G','T']]




N = int(input())
DNA = list(map(str,input().strip()))
now = DNA[-1]
location = N-1
while location > 0:
    
    location -= 1
    x = Table[0].index(DNA[location])
    now = Table[x+1][Table[0].index(now)]
print(now)