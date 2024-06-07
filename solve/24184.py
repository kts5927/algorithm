vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
consonants = set('bcdfghjklmnpqrstvwxyz')

N = int(input().strip())
words = input().strip().split()
def remove_short_vowels(word):
    new_word = []
    length = len(word)
    i = 0
    while i < length:
        if word[i] in vowels:
            if i + 2 < length and word[i+1] in consonants and word[i+2] in consonants:
                i += 1
                continue
        new_word.append(word[i])
        i += 1
    return ''.join(new_word)

processed_words = [remove_short_vowels(word)[::-1] for word in words]
reversed_words = processed_words[::-1]

print(' '.join(reversed_words))
