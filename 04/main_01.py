import re


def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
    return lines


list_valid_passport_fields = ['byr',
                              'hcl',
                              'iyr',
                              'eyr',
                              'hgt',
                              'ecl',
                              'pid']

if __name__ == "__main__":
    valid_passports = 0
    for passport in read_input():
        passport_keys = re.findall(r"([a-z]+):.", passport)
        check = (all(x in passport_keys for x in list_valid_passport_fields))
        if check:
            valid_passports += 1
    print(valid_passports)
