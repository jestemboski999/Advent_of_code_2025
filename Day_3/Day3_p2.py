def best_k_digits (line: str, k: int) -> int:
    pos = 0
    digits = []
    n = len(line)

    remaining = k

    while remaining > 0:
        end_index = n - remaining

        max_val = 0
        best_pos = pos

        for i in range(pos, end_index + 1):
             if int(line[i]) > max_val:
                 max_val = int(line[i])
                 best_pos = i
        
        digits.append(max_val)
        pos = best_pos + 1
        remaining -= 1
    
    value = 0
    for d in digits:
        value = value * 10 + d
    
    return value


def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_3\Day3_input.txt", "r") as fin:
        lines = fin.read().strip().split('\n')
    
    ans = 0

    for line in lines:
        ans +=  best_k_digits(line, 12)

    print (ans)

    
if __name__ == "__main__":
    main()