

def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_3\Day3_input.txt", "r") as fin:
        lines = fin.read().strip().split('\n')
    
    ans = 0

    for line in lines:
        max_val = 1
        pos = 0
        for i in range(len(line) - 1):
            if int(line[i]) > max_val:
                max_val = int(line[i])
                pos = i

        first = max_val
        max_val = 0

        for i in range(pos + 1, len(line)):
            if int(line[i]) > max_val:
                max_val = int(line[i])
        second = max_val
        number = first * 10 + second
        ans += number
        print("number= ", number, "  ans= ", ans)
    
if __name__ == "__main__":
    main()