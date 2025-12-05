from tqdm import tqdm

def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_5\day5_input.txt", "r") as fin:
        lines = fin.read().strip().splitlines()

    blank_index = lines.index('')

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = []
    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    count_fresh = 0

    for line in tqdm(id_lines, desc="Checking IDs"):
        ingredient_id = int(line)
        for start, end in ranges:
            if start <= ingredient_id <= end:
                count_fresh += 1
                break

    print(count_fresh)

if __name__ == "__main__":
    main()
