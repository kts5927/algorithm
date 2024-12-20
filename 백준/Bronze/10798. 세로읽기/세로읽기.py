# 입력 받기
data = [input() for _ in range(5)]

def vertical_read(data):
    result = ""
    for i in range(15): 
        for row in data:
            if i < len(row):  
                result += row[i]
    return result

print(vertical_read(data))
