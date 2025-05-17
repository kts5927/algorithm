def operate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a * b < 0:
            return - (abs(a) // abs(b))
        else:
            return a // b

expr = input().split()
K1, O1, K2, O2, K3 = expr
K1, K2, K3 = int(K1), int(K2), int(K3)

res1 = operate(operate(K1, O1, K2), O2, K3)
res2 = operate(K1, O1, operate(K2, O2, K3))

print(min(res1, res2))
print(max(res1, res2))
