import re


def read_input():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    return lines


def get_row(code):
    rows = list(range(0,128))
    for letter in code:
        if letter == "F":
            rows = rows[:len(rows) // 2]
        elif letter == "B":
            rows = rows[len(rows) // 2:]
    return rows[0]


def get_column(code):
    colummns = list(range(0, 8))
    for letter in code:
        if letter == "L":
            colummns = colummns[:len(colummns) // 2]
        elif letter == "R":
            colummns = colummns[len(colummns) // 2:]
    return colummns[0]


if __name__ == "__main__":
    list_id = []
    for line in read_input():
        row = get_row(line[:7])
        column = get_column(line[7:])
        print(f"ID for row {row} and column {column} is {row*8+column}")
        list_id.append(row*8+column)

    print(f"The highest seat ID is: {max(list_id)}")
