def solution(commands):
    answer = []
    # 병합 상태 저장하는 배열 및 스프레드시트 초기화
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"] * 50 for _ in range(50)]
    
    # 명령어 처리
    for command in commands:
        command = command.split(' ')
        
        if command[0] == 'UPDATE':
            if len(command) == 4:  # 특정 셀 업데이트
                r, c, value = int(command[1])-1, int(command[2])-1, command[3]
                x, y = merged[r][c]
                board[x][y] = value
            elif len(command) == 3:  # 특정 값 전체 업데이트
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            
            # 병합: 빈 셀인 경우 값 복사
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            
            # 두 번째 셀이 가리키는 좌표를 첫 번째 셀로 통일
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
        
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            temp_value = board[x][y]  # 병합된 셀의 값 저장
            
            # 병합된 셀들 모두 분리 및 초기화
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            
            # 분리된 셀의 값 복원
            board[r][c] = temp_value
        
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])
    
    return answer
