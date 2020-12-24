from dataclasses import dataclass

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

cups = get_input("day_23_input")[0]


@dataclass
class Cup:
    id: int
    next_cup: int


all_cups = {}
for index, cup in enumerate(cups):
    if index == len(cups) - 1:
        cup_class = Cup(int(cup), int(cups[0]))
    else:
        cup_class = Cup(int(cup), int(cups[index + 1]))
    all_cups[int(cup)] = cup_class


def order_cups(orig_current, cup_dict):
    results = f"{orig_current}"
    current = orig_current
    while True:
        next_cup = cup_dict[current].next_cup
        results += f"{next_cup}"
        current = next_cup
        if current == orig_current:
            break

    return results


min_cup = min(all_cups)
max_cup = max(all_cups)
current_cup = int(cups[0])


for i in range(100):
    removed_1 = all_cups[current_cup].next_cup
    removed_2 = all_cups[removed_1].next_cup
    removed_3 = all_cups[removed_2].next_cup
    removed = {removed_1, removed_2, removed_3}

    destination_cup = current_cup - 1

    while True:
        if destination_cup < min_cup:
            destination_cup = max_cup

        if destination_cup in removed:
            destination_cup -= 1
            continue

        break

    tmp_next = all_cups[removed_3].next_cup
    all_cups[removed_3].next_cup = all_cups[destination_cup].next_cup
    all_cups[destination_cup].next_cup = all_cups[current_cup].next_cup
    all_cups[current_cup].next_cup = tmp_next

    current_cup = tmp_next

ANSWER1 = answer1(order_cups(1, all_cups)[1:-1])


min_cup = int(min(cups))
max_cup = int(max(cups))


all_cups = {}
for index, cup in enumerate(cups):
    if index == len(cups) - 1:
        cup_class = Cup(int(cup), 10)
    else:
        cup_class = Cup(int(cup), int(cups[index + 1]))
    all_cups[int(cup)] = cup_class

for i in range(10, 1_000_000 + 1):
    if i == 1_000_000:
        cup_class = Cup(i, int(cups[0]))
    else:
        cup_class = Cup(i, i + 1)
    all_cups[i] = cup_class

max_cup = max(all_cups)
current_cup = int(cups[0])

for i in range(10_000_000):
    removed_1 = all_cups[current_cup].next_cup
    removed_2 = all_cups[removed_1].next_cup
    removed_3 = all_cups[removed_2].next_cup
    removed = {removed_1, removed_2, removed_3}

    destination_cup = current_cup - 1

    while True:
        if destination_cup < min_cup:
            destination_cup = max_cup

        if destination_cup in removed:
            destination_cup -= 1
            continue

        break

    tmp_next = all_cups[removed_3].next_cup
    all_cups[removed_3].next_cup = all_cups[destination_cup].next_cup
    all_cups[destination_cup].next_cup = all_cups[current_cup].next_cup
    all_cups[current_cup].next_cup = tmp_next

    current_cup = tmp_next

cup1 = all_cups[1].next_cup
cup2 = all_cups[cup1].next_cup

ANSWER2 = answer2(cup1 * cup2)
