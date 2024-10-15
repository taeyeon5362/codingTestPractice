def expand_space(star_output: list) -> list:
    for x in range(len(star_output)):
        star_output[x].insert(0, " ")
        star_output[x].insert(0, "*")
        star_output[x].append(" ")
        star_output[x].append("*")
    star_output.insert(0, ["*"] + [" "] * (len(star_output[0]) - 1))
    star_output.insert(0, ["*"] * len(star_output[0]))
    star_output.append(["*"] + [" "] * (len(star_output[0]) - 2) + ["*"])
    star_output.append(["*"] * len(star_output[0]))
    return star_output


def print_star(x: int) -> list:
    if x == 1:
        return [["*"]]
    elif x == 2:
        return [
            ["*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " "],
            ["*", " ", "*", "*", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*"],
        ]
    prev_star_output: list = print_star(x - 1)
    prev_star_output = expand_space(prev_star_output)
    prev_star_output[2][-2] = "*"
    return prev_star_output


def main():
    N = int(input())
    star_list = print_star(N)
    for line in map("".join, star_list):
        print(line.rstrip())


if __name__ == "__main__":
    main()