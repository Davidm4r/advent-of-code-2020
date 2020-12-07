import collections

def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
    return lines


def count_yes_per_group(group):
    yes_answers = 0
    list_answers = []
    d = collections.defaultdict(int)
    for person in group.split():
        for answer in person:
            list_answers.append(answer)
            d[answer] += 1
        for key in d.keys():
            if d[key] == len(group.split()):
                yes_answers += 1
    return yes_answers


if __name__ == "__main__":
    number_of_yes = 0
    for group in read_input():
        number_of_yes += count_yes_per_group(group)

    print(number_of_yes)
