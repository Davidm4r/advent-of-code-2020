from itertools import cycle, islice

def read_input():
    with open('test_input.txt') as f:
        lines = f.read().splitlines()[1:]
    return lines


if __name__ == "__main__":
    pos = 1
    tree_count = 0
    moves_to_right = 3
    for column, line in enumerate(read_input()):
        position = (pos%len(line))
        iter = islice(cycle(line), position, None)
        for x in range(moves_to_right-1):
            next(iter)
        last = next(iter)
        print(f"COLUMN: {column}")
        print(f"POSITION: {position}")
        print(f"LINE: {line}")
        print(f"TERRAIN: {last}")
        print("\n")
        pos += moves_to_right
        if last == "#":
            tree_count += 1

    print(tree_count)
