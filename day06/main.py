def pt1(input):
    total = 0
    for x in range(len(input[0])):
        exp = []
        for y in range(len(input) - 1):
            exp.append(input[y][x])
        op = input[-1][x]
        s = f" {op} ".join(exp)
        result = eval(s)
        print(f"Column {x}: {s} = {result}")
        total += result
    print(f"Total: {total}")


def pt2bk(input):
    total = 0
    for x in range(len(input[0])):
        nums = []
        exp = []
        max_len = 0
        for y in range(len(input) - 1):
            n = list(input[y][x])
            nums.append(n)
            max_len = max(max_len, len(n))
        tmp_nums = [*nums]
        nums = []
        for n in tmp_nums:
            while len(n) < max_len:
                n += ["0"]
            print("".join(n))
            nums.append(n)

        for digits in zip(*nums):
            exp.append("int('" + ("".join((digits))) + "')")
            print(exp)
        op = input[-1][x]
        s = f" {op} ".join(exp)
        result = eval(s)
        print(f"Column {x}: {s} = {result}")
        total += result
    print(f"Total: {total}")


def pt2():
    input = [
        list(line)
        for line in open("../input/day6.txt").read().split("\n")
        if line != ""
    ]
    print(input)
    for line in input:
        print("".join(line))
    transposed = list(zip(*(input)))
    print(transposed)
    total = 0
    exp = []
    op = ""

    def acc():
        nonlocal total, exp, op
        e = op.join([c for c in exp if c != "*" and c != "+" and c.strip() != ""])
        print(f"Evaluating: {e}\n")

        total += eval(e)
        exp = []

    for i, line in enumerate(transposed):
        line = "".join(line)
        if len(line.strip()) == 0:
            acc()
            print(line)
        if "*" in line:
            op = "*"
        elif "+" in line:
            op = "+"
        print(f"Line {i}: Operator: {op}, Values: {line}")
        exp.append("".join([c for c in line if c != "*" and c != "+"]))
    acc()
    print(f"Total: {total}")


def main():
    input = [
        [char for char in line.split(" ") if char != ""]
        for line in open("../input/day6.txt").read().strip().split("\n")
    ]
    print(input)
    pt2()


if __name__ == "__main__":
    main()
