import sys
input = sys.stdin.readline

def calculate_love_score(host_count, team_count):
    l = host_count['L'] + team_count['L']
    o = host_count['O'] + team_count['O']
    v = host_count['V'] + team_count['V']
    e = host_count['E'] + team_count['E']

    return ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

def count_love_chars(name):
    count = {char: 0 for char in "LOVE"}
    for char in name:
        if char in count:
            count[char] += 1
    return count

def main():
    yeondu_name = input().strip()
    n = int(input())

    host_count = count_love_chars(yeondu_name)
    team_names = [input().strip() for _ in range(n)]

    best_team = ""
    best_score = -1

    for team_name in sorted(team_names):
        team_count = count_love_chars(team_name)
        score = calculate_love_score(host_count, team_count)

        if score > best_score or (score == best_score and team_name < best_team):
            best_team = team_name
            best_score = score

    print(best_team)

if __name__ == "__main__":
    main()
