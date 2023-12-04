import re

MAX_RED =12
MAX_GREEN=13
MAX_BLUE=14
total=0

def part1(lines):
    for line in lines:
        draws = re.findall(r'(\d+) (blue|red|green)', line)
        impossible = False
        for num in draws:
            # if the number is greater than the max number of balls of that color, it is the game id
            if (int(num[0]) > MAX_RED and num[1] == 'red') or (int(num[0]) > MAX_GREEN and num[1] == 'green') or (int(num[0]) > MAX_BLUE and num[1] == 'blue'):
                impossible=True
                break
        if not impossible:
            # find which game id it is
            game_id = int(re.findall(r'Game (\d+):', line)[0])
            total += game_id
    print(total)


def part2(lines):
    # TODO
    pass


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)


