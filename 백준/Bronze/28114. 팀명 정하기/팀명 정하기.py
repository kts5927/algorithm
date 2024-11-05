team_members = []
for _ in range(3):
    p, y, s = input().split()
    p = int(p) 
    y = int(y)
    team_members.append((p, y, s))

year_mod_100 = sorted([member[1] % 100 for member in team_members])
team_name_1 = ''.join(map(str, year_mod_100))

team_members.sort(key=lambda x: -x[0]) 
team_name_2 = ''.join([member[2][0] for member in team_members])

print(team_name_1)
print(team_name_2)
