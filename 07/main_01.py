import re

def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')
    return lines


def parse_rules_bags(rule):
    list_contain = []
    container_match = re.match(r"(.*?) bags contain", rule)
    container = container_match.group(1)
    contain = re.findall(r"(\d)+ (.*?) bag[s]?", rule)
    for a in contain:
        list_contain.append(a[1])

    return {container: list_contain}

def check_iterations_golden_bag(looking_bags, list_containers, valid_bags):
    count_valid_bags = len(set(valid_bags))
    for looking_bag in looking_bags:
        for bag in list_containers:
            values = list(bag.values())
            if looking_bag in values[0]:
                valid_bags.append(list(bag.keys())[0])
    if count_valid_bags == len(set(valid_bags)):
        print("Number of bags: ", count_valid_bags)
        return
    check_iterations_golden_bag(valid_bags, list_containers, valid_bags)

if __name__ == "__main__":
    golden_bag = ['shiny gold']
    valid_bags = []
    list_containers = []
    for index, rule in enumerate(read_input()):
        list_containers.append(parse_rules_bags(rule))

    check_iterations_golden_bag(golden_bag, list_containers, valid_bags)
