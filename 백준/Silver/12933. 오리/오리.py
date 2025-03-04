duck = list(input().strip())

quack = "quack"
n = len(duck)
visited = [False] * n

if any(duck.count(c) != duck.count('q') for c in quack):
    print(-1)
    exit()

duck_count = 0

def find_duck():
    global duck_count
    sound_index = 0 
    found = False

    for i in range(n):
        if not visited[i] and duck[i] == quack[sound_index]:
            visited[i] = True
            sound_index += 1
            if sound_index == 5: 
                sound_index = 0
                found = True

    if found:
        duck_count += 1
    return found

while True:
    if not find_duck():  
        break

if not all(visited):  
    print(-1)
else:
    print(duck_count)
