from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_16_input")

yours = False
descriptions = {}
nearby_tickets = []
for line in lines:
    if "or" in line:
        description, values = line.split(": ")
        ranges = values.split(" or ")
        testers = []
        for range_ in ranges:
            start, end = range_.split("-")
            testers.append((int(start), int(end)))

        descriptions[description] = testers
    elif line == "":
        continue
    elif "your ticket" in line:
        yours = True
    elif yours is True:
        your_ticket = [int(num) for num in line.split(",")]
        yours = False
    elif "nearby tickets" in line:
        continue
    else:
        nearby_tickets.append([int(num) for num in line.split(",")])


def is_in_testers(num, all_testers):
    for testers in all_testers:
        for start, end in testers:
            if start <= num <= end:
                return True
    return False


invalid = []
validated_tickets = []
for nearby_ticket in nearby_tickets:
    is_valid = True
    for num in nearby_ticket:
        if not is_in_testers(num, descriptions.values()):
            invalid.append(num)
            is_valid = False
    if is_valid:
        validated_tickets.append(nearby_ticket)

ANSWER1 = answer1(sum(invalid))

validated_tickets.append(your_ticket)

description_indexes = {}
for description, testers in descriptions.items():
    possible_indexes = set(range(0, len(your_ticket)))
    for validated_ticket in validated_tickets:
        for index, num in enumerate(validated_ticket):
            if index not in possible_indexes:
                continue

            if not is_in_testers(num, [testers]):
                possible_indexes.remove(index)

        if len(possible_indexes) == 1:
            description_indexes[description] = possible_indexes.pop()
            break
    else:
        description_indexes[description] = possible_indexes

while True:
    has_sets = False
    for description, indexes in description_indexes.items():
        if isinstance(indexes, int):
            continue
        else:
            has_sets = True
            for others in description_indexes.values():
                if isinstance(others, int) and others in indexes:
                    indexes.remove(others)

            if len(indexes) == 1:
                description_indexes[description] = indexes.pop()

    if not has_sets:
        break

total = 1
for description, index in description_indexes.items():
    if "departure" in description:
        total *= your_ticket[index]

ANSWER2 = answer2(total)
