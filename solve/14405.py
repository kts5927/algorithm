pkc = {'p':['p','i'],'k':['k','a'],'c':['c','h','u']}
pika = list(map(str, input().strip()))

i = 0
while i < len(pika):
    if pika[i] in pkc:
        seq = pkc[pika[i]]
        for j in seq:
            if i >= len(pika) or pika[i] != j:
                print('NO')
                exit()
            i += 1
    else:
        print('NO')
        exit()
print('YES')
