def solution(commands):
    answer = []
    
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    Table = [['EMPTY'] * 50 for _ in range(50)]
    
    for data in commands:
        command = data.split()
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r = int(command[1]) - 1
                c = int(command[2]) - 1
                Value = command[3]
                
                # 병합된 셀 처리
                x, y = merged[r][c]
                Table[x][y] = Value
                
            elif len(command) == 3:
                Value1, Value2 = command[1], command[2]
                
                # Table 전체 탐색하여 값 변경
                for i in range(50):
                    for j in range(50):
                        if Table[i][j] == Value1:
                            Table[i][j] = Value2
        
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            
            # 병합: 빈 셀인 경우 값 복사
            if Table[x1][y1] == "EMPTY":
                Table[x1][y1] = Table[x2][y2]
            
            # 두 번째 셀이 가리키는 좌표를 첫 번째 셀로 통일
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
            
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            temp_value = Table[x][y]  # 병합된 셀의 값 저장
            
            # 병합된 셀들 모두 분리 및 초기화
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        Table[i][j] = "EMPTY"
            
            # 분리된 셀의 값 복원
            Table[r][c] = temp_value
            
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(Table[x][y])
    
    return answer
