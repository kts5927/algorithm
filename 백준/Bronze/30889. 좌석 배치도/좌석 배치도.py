N = int(input())
theater = [['.']*20 for _ in range(10)]
for i in range(N):
    seat = input().strip()
    theater[ord(seat[0]) - ord('A')][int(seat[1:])-1] = 'o'
    
for i in theater:
    print(''.join(i))
    