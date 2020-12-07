import re


class Validator(object):
    def validate_byr(self, value):
        if not len(value) == 4:
            return False
        elif 1920 <= int(value) <= 2002:
            return True
        else:
            return False

    def validate_iyr(self, value):
        if not len(value) == 4:
            return False
        elif 2010 <= int(value) <= 2020:
            return True
        else:
            return False

    def validate_eyr(self, value):
        if not len(value) == 4:
            return False
        elif 2020 <= int(value) <= 2030:
            return True
        else:
            return False

    def validate_hgt(self, value):
        hgt = re.match(r"(\d+)(\w+)", value)
        if hgt.group(2) == "cm":
            if 150 <= int(hgt.group(1)) <= 193:
                return True
            else:
                return False
        elif hgt.group(2) == "in":
            if 59 <= int(hgt.group(1)) <= 76:
                return True
            else:
                return False
        else:
            return False

    def validate_hcl(self, value):
        hcl = re.match(r"#([0-9]{6})", value)
        if hcl:
            return True
        else:
            if re.match(r"#([a-f]{6})", value):
                return True
            else:
                return False

    def validate_ecl(self, value):
        accepted_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value in accepted_values:
            return True
        else:
            return False

    def validate_pid(self, value):
        if re.match(r"([\d]{9})", value):
            return True
        else:
            return False

    def validate_cid(self, value):
        return True


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


def valid_value_key_passport(key, value):
    validator = Validator()
    return getattr(validator, 'validate_%s' % key)(value)


if __name__ == "__main__":
    valid_passports = 0
    a=0
    for passport in read_input():
        passport_keys_values = re.findall(r"([a-z]+):([^\s]+)", passport)
        list_passport_keys = list(map(list, zip(*passport_keys_values)))
        print(list_passport_keys)
        print("A")
        check = (all(x in list_passport_keys[0] for x in list_valid_passport_fields))
        a+=1
        if check:
            for index, _ in enumerate(list_passport_keys[0]):
                check_validation = valid_value_key_passport(list_passport_keys[0][index], list_passport_keys[1][index])
                print(f"key: {list_passport_keys[0][index]} value: {list_passport_keys[1][index]} {check_validation}")
                if check_validation:
                    if index >= len(list_passport_keys[0])-1:
                        valid_passports += 1
                    continue
                else:
                    break

    print(valid_passports)
    print(a) # 206
