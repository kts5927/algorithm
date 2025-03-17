import sys

def convert(value, unit):
    conversion = {
        "kg": (2.2046, "lb"),
        "lb": (0.4536, "kg"),
        "l": (0.2642, "g"),
        "g": (3.7854, "l")
    }
    
    factor, new_unit = conversion[unit]
    return round(value * factor, 4), new_unit

def main():
    T = int(sys.stdin.readline().strip())
    
    for _ in range(T):
        data = sys.stdin.readline().split()
        value, unit = float(data[0]), data[1]
        converted_value, converted_unit = convert(value, unit)
        print(f"{converted_value:.4f} {converted_unit}")

if __name__ == "__main__":
    main()