def binary_bitwise_operations(a: str, b: str):
    int_a = int(a, 2)
    int_b = int(b, 2)
    n = len(a)

    result_and = bin(int_a & int_b)[2:].zfill(n)
    result_or = bin(int_a | int_b)[2:].zfill(n)
    result_xor = bin(int_a ^ int_b)[2:].zfill(n)
    result_not_a = bin(~int_a & ((1 << n) - 1))[2:].zfill(n)
    result_not_b = bin(~int_b & ((1 << n) - 1))[2:].zfill(n)

    print(result_and)
    print(result_or)
    print(result_xor)
    print(result_not_a)
    print(result_not_b)

a = input().strip()
b = input().strip()

binary_bitwise_operations(a, b)
