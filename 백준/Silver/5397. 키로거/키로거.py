import sys
input = sys.stdin.readline

def sol():
    T = int(input())
    for _ in range(T):
        command = input().strip()
        left = []
        right = []

        for c in command:
            if c == '<':
                if left:
                    right.append(left.pop())
            elif c == '>':
                if right:
                    left.append(right.pop())
            elif c == '-':
                if left:
                    left.pop()
            else:
                left.append(c)
        
        left.extend(reversed(right))
        print(''.join(left))

sol()
