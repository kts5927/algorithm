R, S = map(int, input().split())
church = [list(input().strip()) for _ in range(R)]

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 현재 악수 수
current_handshakes = 0
for i in range(R):
    for j in range(S):
        if church[i][j] == 'o':
            for d in range(8):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < R and 0 <= nj < S and church[ni][nj] == 'o':
                    current_handshakes += 1
current_handshakes //= 2

max_new_handshakes = 0
for i in range(R):
    for j in range(S):
        if church[i][j] == '.':
            cnt = 0
            for d in range(8):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < R and 0 <= nj < S and church[ni][nj] == 'o':
                    cnt += 1
            if cnt > max_new_handshakes:
                max_new_handshakes = cnt

print(current_handshakes + max_new_handshakes)
