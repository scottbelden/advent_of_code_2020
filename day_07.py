from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

my_bag = "shiny gold"

rules = {}
does_not_contain_shiny_gold = set()
contains_shiny_gold = set()

for rule in get_input("day_07_input"):
    start, end = rule.split(" contain ")
    start_bag = start.rsplit(" ", 1)[0]

    if "no other bags" in rule:
        does_not_contain_shiny_gold.add(start_bag)
    else:
        others = set()
        for other in end.split(", "):
            num, adj, color, _ = other.split()
            others.add(f"{adj} {color}")

        rules[start_bag] = others

while rules:
    new_rules = {}

    for bag, contents in rules.items():
        new_contents = set()
        for inside_bag in contents:
            if inside_bag in contains_shiny_gold or inside_bag == my_bag:
                contains_shiny_gold.add(bag)
                break
            elif inside_bag in does_not_contain_shiny_gold:
                continue
            else:
                new_contents.add(inside_bag)
        else:
            if new_contents:
                new_rules[bag] = new_contents
            else:
                does_not_contain_shiny_gold.add(bag)

    rules = new_rules

ANSWER1 = answer1(len(contains_shiny_gold))

rules = {}
for rule in get_input("day_07_input"):
    start, end = rule.split(" contain ")
    start_bag = start.rsplit(" ", 1)[0]

    if "no other bags" in rule:
        rules[start_bag] = 0
    else:
        others = {}
        for other in end.split(", "):
            num, adj, color, _ = other.split()
            others[f"{adj} {color}"] = int(num)

        rules[start_bag] = others


def get_num_bags(rules, color):
    if isinstance(rules[color], int):
        return rules[color]
    else:
        total = 0
        for inside_color, quantity in rules[color].items():
            total += quantity + (quantity * get_num_bags(rules, inside_color))
        rules[color] = total
        return total


ANSWER2 = answer2(get_num_bags(rules, my_bag))
