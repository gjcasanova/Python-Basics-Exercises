rules = (
        (8, 7),
        (10, 9),
        (12, 13),
        (14, 15),
)


def cercanias(line, direction):
    if direction not in ('N', 'S') or not (0 <= line <= 3):
        return 0

    direction_idx = 0 if direction == 'N' else 1

    return rules[line][direction_idx]


def main():
    line, direction = input().split()
    line = int(line) - 1
    ans = cercanias(line, direction)
    print(ans)


if __name__ == '__main__':
    main()
