def is_invalid_id2(n: int) -> bool:
    number = str(n)
    L = len(number)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        
        repeat = L // k
        chunk = number[:k]
        if number == chunk * repeat:
            return True
        
    return False


def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_2\day2_input.txt", "r") as fin:
        ranges = fin.read().strip().split(',')

    invalid_combinations = set()

    for line in ranges:
        #print(line)
        number1, number2 = line.split('-')
        #print(number1,'+', number2)

        start = int(number1)
        end = int(number2)

        for n in range(start, end+1):
            #print("i=", i, "start=", start, "end=", end)
            if is_invalid_id2(n):
                invalid_combinations.add(n)
                #print(n)

    print("ANS1 = ", sum(invalid_combinations))

if __name__ == "__main__":
    main()