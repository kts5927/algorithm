from collections import Counter

N = int(input())
files = [input().strip() for _ in range(N)]

extensions = [file.split('.')[-1] for file in files]
extension_count = Counter(extensions)

for ext, count in sorted(extension_count.items()):
    print(ext, count)
