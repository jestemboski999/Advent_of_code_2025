def turn_dial(pos, direction, steps):
    zero_hits = 0
    for _ in range (steps):
        if (direction == 'R'):
            pos = (pos + 1) % 100
        else :
            pos = (pos - 1) % 100

        if pos == 0:
            zero_hits += 1

    print(direction, steps, "->", pos)
    return pos, zero_hits


def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_1\day1_input.txt", "r") as fin:
        lines = fin.read().strip().split("\n")

    ans2 = 0
    pos = 50

    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        full_rotations = steps // 100
        rest = steps % 100
        ans2 += full_rotations
        pos, zero_hits = turn_dial(pos, direction, rest)
        ans2 += zero_hits

    print("ANS2: ", ans2)

if __name__ == "__main__":
    main()
