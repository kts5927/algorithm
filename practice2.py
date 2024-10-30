import random
a = 0
b = 0
Mb = 10000
MMb = 0
Ms = 10000
MMs = 0
for i in range(10000):
    count = 0
    spell = 0
    while True:

        Try = 0
        enforce = 0
        while enforce < 7:

            A = random.randrange(1,10)
            Try += 1
            spell += 1
            if A-6 > 0:
                enforce += 1
            else:
                break
        count += 1
        if enforce == 7:
            Mb = min(count,Mb)
            MMb = max(count,MMb)
            Ms = min(spell,Ms)
            MMs = max(count,MMs)
            a += count
            b += spell
            print('터뜨린 장비 : ',count)
            print('주문서 개수 : ',spell)
            break
print('장비평균 : ',a//10000)
print('최소 장비 : ',Mb)
print('최대 장비 : ',MMb)
print('주문서 평균 : ',b//10000)
print('최소 주문서 : ',Ms)
print('최대 주문서 : ',MMs)