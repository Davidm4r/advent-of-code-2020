import re


def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def check_valid_password(min_ocurrence, max_ocurrence, letter, password):
    count = password.count(letter)
    if int(min_ocurrence) <= count <= int(max_ocurrence):
        return True
    else:
        return False


def password_policy(line):
    line = line.split()
    min_max_string = re.search(r'(\d+)-(\d+)', line[0])
    min_ocurrence = min_max_string.group(1)
    max_ocurrence = min_max_string.group(2)
    letter = re.search(r'([a-z]):', line[1]).group(1)
    password = re.search(r'([a-z]+$)', line[2]).group(1)

    return check_valid_password(min_ocurrence, max_ocurrence, letter, password)


if __name__ == "__main__":
    number_valid_passwords = 0
    for line in read_input():
        if password_policy(line):
            number_valid_passwords += 1

    print(number_valid_passwords)
