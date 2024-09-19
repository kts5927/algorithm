import sys

def solution():
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    while True:
        count = int(data[index])
        index += 1
        
        if count == 0:
            break
        
        power_station = []
        for i in range(count):
            power_station.append(int(data[index]))
            index += 1
        
        power_station.sort()
        
        # 도착지까지 갈 수 있는지 체크
        distance = 0
        possible = True
        for station in power_station:
            if station <= distance:
                distance = station + 200
            else:
                possible = False
                break
        
        # 델타 정션까지 갈 수 있는지 확인
        if possible and distance >= 1422:
            # 왕복할 때 마지막 충전소에서 델타 정션(1422)까지의 거리 확인
            distance -= 1422
            if distance >= 1422 - power_station[-1]:
                print("POSSIBLE")
            else:
                print("IMPOSSIBLE")
        else:
            print("IMPOSSIBLE")

if __name__ == "__main__":
    solution()
