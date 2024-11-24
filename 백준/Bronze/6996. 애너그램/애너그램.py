def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
test_cases = int(input())
results = []

for _ in range(test_cases):
    word1, word2 = input().split()
    if are_anagrams(word1, word2):
        results.append(f"{word1} & {word2} are anagrams.")
    else:
        results.append(f"{word1} & {word2} are NOT anagrams.")
for result in results:
    print(result)
