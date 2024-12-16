import sys

input_line = sys.stdin.readline().strip()
S1, S2, S3 = map(int, input_line.split())

sumCount = {}

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            sum_value = i + j + k
            if sum_value not in sumCount:
                sumCount[sum_value] = 1
            else:
                sumCount[sum_value] += 1

maxFrequency = 0
result = 0

for sumKey, frequency in sumCount.items():
    if frequency > maxFrequency:
        maxFrequency = frequency
        result = sumKey
    elif frequency == maxFrequency and sumKey < result:
        result = sumKey

print(result)