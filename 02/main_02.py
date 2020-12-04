import re


def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def check_valid_password(first_position, second_position, letter, password):
    letter_first_position = password[int(first_position) - 1]
    letter_second_position = password[int(second_position) - 1]
    if letter_first_position == letter and letter_second_position == letter:
        return False
    elif letter_first_position == letter:
        return True
    elif letter_second_position == letter:
        return True
    else:
        return False


def password_policy(line):
    line = line.split()
    min_max_string = re.search(r'(\d+)-(\d+)', line[0])
    first_position = min_max_string.group(1)
    second_position = min_max_string.group(2)
    letter = re.search(r'([a-z]):', line[1]).group(1)
    password = re.search(r'([a-z]+$)', line[2]).group(1)

    return check_valid_password(first_position, second_position, letter, password)


if __name__ == "__main__":
    number_valid_passwords = 0
    for line in read_input():
        if password_policy(line):
            number_valid_passwords += 1

    print(number_valid_passwords)
