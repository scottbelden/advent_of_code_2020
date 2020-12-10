from collections import defaultdict

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

jolt_adapters = [int(num) for num in get_input("day_10_input")]

ordered_jolt_adapters = sorted(jolt_adapters)
ordered_jolt_adapters.insert(0, 0)
ordered_jolt_adapters.append(ordered_jolt_adapters[-1] + 3)

diffs = defaultdict(int)
for index, jolt_adapter in enumerate(ordered_jolt_adapters):
    if index + 1 == len(ordered_jolt_adapters):
        break

    diff = ordered_jolt_adapters[index + 1] - jolt_adapter
    diffs[diff] += 1

ANSWER1 = answer1(diffs[1] * diffs[3])

groups = []
group = []
current_index = 0
while current_index < len(ordered_jolt_adapters) - 1:
    if (
        ordered_jolt_adapters[current_index + 1] - ordered_jolt_adapters[current_index]
        < 3
    ):
        if group:
            group.append(ordered_jolt_adapters[current_index + 1])
        else:
            group.append(ordered_jolt_adapters[current_index])
            group.append(ordered_jolt_adapters[current_index + 1])
    else:
        groups.append(group)
        group = []

    current_index += 1

path_map = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 7,
}
total_paths = 1
for group in groups:
    total_paths *= path_map[len(group)]

ANSWER2 = answer2(total_paths)
