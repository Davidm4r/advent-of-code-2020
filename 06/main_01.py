

def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
    return lines


def count_yes_per_group(group):
    yes_answers = set()
    for person in group:
        yes_answers.add(person)
    if "\n" in yes_answers:
        yes_answers.remove("\n")
    return len(yes_answers)


if __name__ == "__main__":
    number_of_yes = 0
    for group in read_input():
        number_of_yes += count_yes_per_group(group)

    print(number_of_yes)
