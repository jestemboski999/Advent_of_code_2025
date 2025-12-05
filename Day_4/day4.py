def count_neighbours(r: int, c: int, lines, rows, cols) -> int:
    neighbours = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1) ]
    
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue

        if lines[nr][nc] == '@':
            neighbours += 1

    return neighbours

def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_4\day4_input.txt", "r") as fin:
        lines = fin.read().strip().splitlines()

    rows = len(lines)
    cols = len(lines[0])
    
    ans = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '@':
                neighbours = count_neighbours(r, c, lines, rows, cols)
                if neighbours < 4:
                    ans += 1

    print(ans)
    
if __name__ == "__main__":
    main()