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

def check_empty_seat(seats):
    for index, seat in enumerate(seats):
        try:
            if seat -1 == seats[index-1] and seat +1 == seats[index+1]:
                pass
            elif index != 0:
                print(f"Your seat is close to {seat}")
        except IndexError as e:
            pass

if __name__ == "__main__":
    list_id = []
    for line in read_input():
        row = get_row(line[:7])
        column = get_column(line[7:])
        print(f"ID for row {row} and column {column} is {row*8+column}")
        list_id.append(row*8+column)

    # Order the list by id
    list_id.sort()
    check_empty_seat(list_id)
