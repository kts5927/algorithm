def eval_check(expression):
    if not expression.isdigit():
        raise ValueError("정수만 입력할 수 있습니다.")
    
    print(eval(expression))

try:
    result = eval_check("123") 
    result = eval_check("123.45")
except ValueError as e:
    print(e)