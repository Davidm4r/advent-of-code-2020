from functools import reduce
from itertools import cycle, islice


def read_input():
    with open('input.txt') as f:
        lines = f.read().splitlines()[1:]
    return lines


list_of_slopes = [
    {"right": 1,
     "down": 1},

    {"right": 3,
     "down": 1},

    {"right": 5,
     "down": 1},

    {"right": 7,
     "down": 1},

    {"right": 1,
     "down": 2},
]

if __name__ == "__main__":
    list_of_trees = []
    for slope in list_of_slopes:
        pos = 1
        tree_count = 0
        moves_to_right = slope["right"]
        moves_to_down = slope["down"]
        for column, line in enumerate(read_input()):
            if (column+1) % moves_to_down == 0:
                position = (pos % len(line))
                iter = islice(cycle(line), position, None)
                for x in range(moves_to_right - 1):
                    next(iter)
                last = next(iter)
                pos += moves_to_right
                if last == "#":
                    tree_count += 1
            else:
                continue

        print(tree_count)
        list_of_trees.append(tree_count)

    print(reduce((lambda x, y: x * y), list_of_trees))
