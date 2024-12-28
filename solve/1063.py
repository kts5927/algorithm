import sys
input = sys.stdin.readline

def EngToNum(a):
    return [ord(a.strip()[0]) - ord('A'), int(a.strip()[1]) - 1]

def Command(King, Stone, command):
    for i in range(8):
        if command == move[i]:
            new_king = [King[0] + LR[i], King[1] + UD[i]]

            if 0 <= new_king[0] < 8 and 0 <= new_king[1] < 8:
                if new_king == Stone:
                    new_stone = [Stone[0] + LR[i], Stone[1] + UD[i]]
                    if 0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8:
                        King[0], King[1] = new_king
                        Stone[0], Stone[1] = new_stone
                else:
                    King[0], King[1] = new_king

King, Stone, N = input().split()
move = ['R', 'RT', 'T', 'LT', 'L', 'LB', 'B', 'RB']

King = EngToNum(King)
Stone = EngToNum(Stone)

UD = [0, 1, 1, 1, 0, -1, -1, -1]
LR = [1, 1, 0, -1, -1, -1, 0, 1]

for _ in range(int(N)):
    command = input().strip()
    Command(King, Stone, command)

def NumToEng(pos):
    return chr(pos[0] + ord('A')) + str(pos[1] + 1)

print(NumToEng(King))
print(NumToEng(Stone))
