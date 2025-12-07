def prase_fresh(fresh):
    return [
        tuple([int(line.split("-")[0]), int(line.split("-")[1])])
        for line in fresh.split("\n")
    ]


def parse_ingredients(refs):
    return [int(x) for x in refs.split("\n")]


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_overlapping(self, other):
        return self.start <= other.end and other.start <= self.end

    def merge(self, other):
        if not self.is_overlapping(other):
            return None
        return Range(min(self.start, other.start), max(self.end, other.end))


def main():
    input = open("../input/day5.txt").read().strip().split("\n\n")
    [fresh, refs] = input
    fresh = prase_fresh(fresh)
    ing = parse_ingredients(refs)
    count = 0
    for i in ing:
        for start, end in fresh:
            if start <= i <= end:
                count += 1
                break
    print(count)


def main2():
    input = open("../input/day5.txt").read().strip().split("\n\n")
    [fresh, refs] = input
    fresh = prase_fresh(fresh)
    all_fresh_count = 0

    sorted_fresh = sorted(fresh, key=lambda x: x[0])
    ranges = [Range(start, end) for start, end in sorted_fresh]
    final_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        last = final_ranges[-1] if final_ranges else ranges[0]
        merged = last.merge(ranges[i])
        if merged:
            final_ranges[-1] = merged
        else:
            final_ranges.append(ranges[i])

    total_covered = sum(r.end - r.start + 1 for r in final_ranges)
    print(total_covered)


if __name__ == "__main__":
    main2()
