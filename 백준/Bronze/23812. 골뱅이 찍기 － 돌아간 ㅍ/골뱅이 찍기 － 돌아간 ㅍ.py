def print_rotated_P(N):
    for block in range(5):
        for _ in range(N):
            if block % 2 == 0:
                line = "@" * N + " " * (3 * N) + "@" * N
            else:
                line = "@" * (5 * N)
            print(line)

if __name__ == "__main__":
    N = int(input())
    print_rotated_P(N)
