import sys
input = sys.stdin.readline
Max = 29

def Querry(Hash,querry,num):
    if querry == 1:
        Querry_1(Hash,num)
    elif querry == 2:
        Querry_2(Hash,num)
    elif querry == 3:
        Querry_3(Hash,num)
        

def Querry_1(Hash,num):
    now = Hash
    for i in range(Max,-1,-1):
        cal = 1 if num & (1 <<i ) else 0
        if cal not in now:
            now[cal] = {2:1} # 0이랑 1로만 데이터를 표현하기 때문에 count를 2에 표시
        else:
            now[cal][2] += 1
        now = now[cal]



def Querry_2(Hash,num):
    now  = Hash
    for i in range(Max,-1,-1) :
        cal = 1 if num & (1 << i) else 0
        now[cal][2] -= 1
        if not now[cal][2]:
            del now[cal]
            return
        now = now[cal]
            

def Querry_3(Hash,num):
    now = Hash
    ans = 0
    for i in range(Max,-1,-1) :
        pointer = num & (1 << i)
        _range = [0,1] if num & (1 << i) else [1,0]
        for j in _range:
            if j in now:
                break
        if j and not pointer or not j and pointer:
            ans += 1 << i
        now = now[j]
    print(ans)



M = int(input())
Hash = {}
Querry(Hash,1,0)
for i in range(M):
    querry , num = map(int,input().split())
    Querry(Hash,querry,num)
    