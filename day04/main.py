def count_connected(lines, y, x):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]):
                if lines[ny][nx] == "@":
                    count += 1
    return count


def main():
    input = open("../input/day4.txt").read().strip().split("\n")

    lines = [list(x) for x in input if x != ""]
    total_removed = 0
    previous_removed = -1
    while previous_removed != total_removed:
        previous_removed = total_removed
        removed = 0
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] != "@":
                    continue
                c = count_connected(lines, y, x)
                if c < 4:
                    removed += 1
                    total_removed += 1
                    lines[y][x] = "."

    print(total_removed)


if __name__ == "__main__":
    main()
