import sys

# 거울 대응표
mirror = {
    'b': 'd', 'd': 'b',
    'p': 'q', 'q': 'p',
    'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x',
}

def convert(word: str) -> str:
    try:
        # 1) 문자 변환  2) 뒤집기
        converted = ''.join(mirror[c] for c in word)[::-1]
        return converted
    except KeyError:
        return 'INVALID'

def main() -> None:
    for line in sys.stdin:
        word = line.strip()
        if word == '#':
            break
        print(convert(word))

if __name__ == '__main__':
    main()