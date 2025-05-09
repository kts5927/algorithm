N = int(input()) 
friends = [list(input().strip()) for _ in range(N)] 
max_friends = 0

for i in range(N):
    friends_of_i = set()
    
    for j in range(N):
        if friends[i][j] == 'Y':
            friends_of_i.add(j)
    
    for friend in list(friends_of_i):
        for k in range(N):
            if friends[friend][k] == 'Y' and k != i:
                friends_of_i.add(k)

    max_friends = max(max_friends, len(friends_of_i))

print(max_friends)
