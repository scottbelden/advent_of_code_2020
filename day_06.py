from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

groups = []
group = set()
for line in get_input("day_06_input"):
    if line == "":
        groups.append(group)
        group = set()

    group = group | set(line)

if group:
    groups.append(group)

ANSWER1 = answer1(sum([len(group) for group in groups]))

groups = []
mini_group = []
for line in get_input("day_06_input"):
    if line == "":
        groups.append(set.intersection(*mini_group))
        mini_group = []
        continue

    mini_group.append(set(line))

if mini_group:
    groups.append(set.intersection(*mini_group))

ANSWER2 = answer2(sum([len(group) for group in groups]))
