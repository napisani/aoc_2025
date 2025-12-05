def process_range(r):
    [start, end] = [int(x) for x in r.split("-")]
    silly = []
    print(f"Processing range: {start} to {end}")
    for i in range(start, end + 1):
        s = f"{i}"
        if len(s) % 2 != 0:
            continue
        mid = len(s) // 2
        left, right = s[:mid], s[mid:]
        if left == right:
            silly.append(i)

    return silly


def process_range_pt2(r):
    [start, end] = [int(x) for x in r.split("-")]
    silly = []
    print(f"Processing range: {start} to {end}")
    for i in range(start, end + 1):
        s = f"{i}"
        for div in range(1, len(s) // 2 + 1):
            parts = {s[j : j + div] for j in range(0, len(s), div)}
            if len(parts) == 1:
                silly.append(i)
                break

    return silly


def main():
    input = open("../input/day2.txt").read().strip().split(",")

    ranges = [r for x in input for r in process_range_pt2(x)]

    print(ranges)
    print(len(ranges))
    print(sum(ranges))


if __name__ == "__main__":
    main()
