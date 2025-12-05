def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_5\day5_input.txt", "r") as fin:
        lines = fin.read().strip().splitlines()

    blank_index = lines.index('')

    range_lines = lines[:blank_index]
    # dolna część pliku nas teraz nie interesuje

    ranges = []
    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    # sortujemy zakresy po początku
    ranges.sort()

    # mergujemy zakresy
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                # nakłada się lub styka -> łączymy
                merged[-1][1] = max(last_end, end)
            else:
                # osobny zakres
                merged.append([start, end])

    # liczymy, ile ID jest świeżych łącznie
    total_fresh = 0
    for start, end in merged:
        total_fresh += end - start + 1

    print(total_fresh)


if __name__ == "__main__":
    main()
