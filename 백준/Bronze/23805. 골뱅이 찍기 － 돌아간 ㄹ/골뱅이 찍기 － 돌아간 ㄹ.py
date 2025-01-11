N = int(input())

for i in range(N):
    print(''.join(['@'*N,'@'*N,'@'*N,' '*N,'@'*N]))
for i in range(N):
    for j in range(3):
        print(''.join(['@'*N,' '*N,'@'*N,' '*N,'@'*N]))
for i in range(N):
    print(''.join(['@'*N,' '*N,'@'*N,'@'*N,'@'*N]))