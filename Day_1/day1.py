def turn_dial(pos, direction, steps):
    if (direction == 'R'):
        new_pos = (pos + steps) % 100
    else :
        new_pos = (pos - steps) % 100

    print(direction, steps, "->", new_pos)
    return new_pos


def main():
    with open(r"C:\Users\filip\OneDrive\Programy\Advent_of_code_2025\Day_1\day1_input.txt", "r") as fin:
        lines = fin.read().strip().split("\n")

    ans1 = 0
    pos = 50

    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        pos = turn_dial(pos, direction, steps)
        if (pos == 0):
            ans1 += 1

    print("ANS1: ", ans1)

if __name__ == "__main__":
    main()
