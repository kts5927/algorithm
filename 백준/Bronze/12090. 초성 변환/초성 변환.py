def cal(S):
    table = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    ans = ""

    for String in S:
        if '가' <= String <= '힣':
            code = ord(String) - 0xAC00
            index = code // (21 * 28)
            ans += table[index]
    
    return ans

S = input().strip()
print(cal(S))
