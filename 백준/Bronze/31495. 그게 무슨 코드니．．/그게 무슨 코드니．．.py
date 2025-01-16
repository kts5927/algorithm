S = input().strip()

if S.startswith('"') and S.endswith('"'):
    if len(S) > 2:
        print(S[1:-1])
    else:
        print("CE")
else:
    print("CE")
