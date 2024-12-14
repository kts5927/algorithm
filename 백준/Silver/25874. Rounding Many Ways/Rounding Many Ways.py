def main():
    N = int(input().strip())
    valid_x = set()
    power_of_two = [1]
    power_of_five = [1]
    
    while power_of_two[-1] <= N:
        power_of_two.append(power_of_two[-1] * 2)
    while power_of_five[-1] <= N:
        power_of_five.append(power_of_five[-1] * 5)

    for a in power_of_two:
        for b in power_of_five:
            x = a * b
            if x > N:
                break
            if N % x == 0:
                valid_x.add(x)
    
    valid_x = sorted(valid_x)
    print(len(valid_x))
    for x in valid_x:
        print(x)

if __name__ == "__main__":
    main()
