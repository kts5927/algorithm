T = int(input())  
for _ in range(T):
    line = input().strip() 
    operand1, operator, operand2, _, result = line.split()
    operand1 = int(operand1)
    operand2 = int(operand2)
    result = int(result)
    
    if operator == '+':
        calc_result = operand1 + operand2
    elif operator == '-':
        calc_result = operand1 - operand2
    elif operator == '*':
        calc_result = operand1 * operand2
    elif operator == '/':
        calc_result = operand1 // operand2  # 나눗셈은 항상 나누어 떨어진다고 했으므로 정수 나눗셈
    
    if calc_result == result:
        print("correct")
    else:
        print("wrong answer")
