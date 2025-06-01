import sys

def main():
    input = sys.stdin.readline

    N = int(input().strip())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    answer = 10**40

    x_min = 10**40
    x_max = -10**40
    y_min = 10**40
    y_max = -10**40
    for i in range(N):
        x_min = min(x_min, points[i][0])
        x_max = max(x_max, points[i][0])
        y_min = min(y_min, points[i][1])
        y_max = max(y_max, points[i][1])
    x_span = x_max - x_min
    y_span = y_max - y_min
    L = max(x_span, y_span) + 2
    area = L * L
    answer = min(answer, area)

    for exclude in range(N):
        x_min = 10**40
        x_max = -10**40
        y_min = 10**40
        y_max = -10**40
        for i in range(N):
            if i == exclude:
                continue
            x_min = min(x_min, points[i][0])
            x_max = max(x_max, points[i][0])
            y_min = min(y_min, points[i][1])
            y_max = max(y_max, points[i][1])
        x_span = x_max - x_min
        y_span = y_max - y_min
        L = max(x_span, y_span) + 2
        area = L * L
        answer = min(answer, area)

    for i in range(N):
        for j in range(i + 1, N):
            x_min = 10**40
            x_max = -10**40
            y_min = 10**40
            y_max = -10**40
            for k in range(N):
                if k == i or k == j:
                    continue
                x_min = min(x_min, points[k][0])
                x_max = max(x_max, points[k][0])
                y_min = min(y_min, points[k][1])
                y_max = max(y_max, points[k][1])
            x_span = x_max - x_min
            y_span = y_max - y_min
            L = max(x_span, y_span) + 2
            area = L * L
            answer = min(answer, area)

    print(answer)

if __name__ == "__main__":
    main()
