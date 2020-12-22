from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_17_input")

active = set()
for y_index, line in enumerate(lines):
    for x_index, char in enumerate(line):
        if char == "#":
            active.add((x_index, y_index, 0))


def should_be_active(x, y, z, active_set):
    currently_active = (x, y, z) in active_set
    neighbors_active = 0

    for other_x in (x - 1, x, x + 1):
        for other_y in (y - 1, y, y + 1):
            for other_z in (z - 1, z, z + 1):
                if other_x == x and other_y == y and other_z == z:
                    continue

                if (other_x, other_y, other_z) in active_set:
                    neighbors_active += 1
                    if neighbors_active > 3:
                        return False

    if currently_active and (neighbors_active == 2 or neighbors_active == 3):
        return True
    elif not currently_active and neighbors_active == 3:
        return True
    else:
        return False


for i in range(6):
    min_x = min(coord[0] for coord in active)
    max_x = max(coord[0] for coord in active)
    min_y = min(coord[1] for coord in active)
    max_y = max(coord[1] for coord in active)
    min_z = min(coord[2] for coord in active)
    max_z = max(coord[2] for coord in active)

    new_actives = set()
    for test_x in range(min_x - 1, max_x + 2):
        for test_y in range(min_y - 1, max_y + 2):
            for test_z in range(min_z - 1, max_z + 2):
                if should_be_active(test_x, test_y, test_z, active):
                    new_actives.add((test_x, test_y, test_z))

    active = new_actives

ANSWER1 = answer1(len(active))

active = set()
for y_index, line in enumerate(lines):
    for x_index, char in enumerate(line):
        if char == "#":
            active.add((x_index, y_index, 0, 0))


def should_be_active(x, y, z, w, active_set):
    currently_active = (x, y, z, w) in active_set
    neighbors_active = 0

    for other_x in (x - 1, x, x + 1):
        for other_y in (y - 1, y, y + 1):
            for other_z in (z - 1, z, z + 1):
                for other_w in (w - 1, w, w + 1):
                    if other_x == x and other_y == y and other_z == z and other_w == w:
                        continue

                    if (other_x, other_y, other_z, other_w) in active_set:
                        neighbors_active += 1
                        if neighbors_active > 3:
                            return False

    if currently_active and (neighbors_active == 2 or neighbors_active == 3):
        return True
    elif not currently_active and neighbors_active == 3:
        return True
    else:
        return False


for i in range(6):
    min_x = min(coord[0] for coord in active)
    max_x = max(coord[0] for coord in active)
    min_y = min(coord[1] for coord in active)
    max_y = max(coord[1] for coord in active)
    min_z = min(coord[2] for coord in active)
    max_z = max(coord[2] for coord in active)
    min_w = min(coord[3] for coord in active)
    max_w = max(coord[3] for coord in active)

    new_actives = set()
    for test_x in range(min_x - 1, max_x + 2):
        for test_y in range(min_y - 1, max_y + 2):
            for test_z in range(min_z - 1, max_z + 2):
                for test_w in range(min_w - 1, max_w + 2):
                    if should_be_active(test_x, test_y, test_z, test_w, active):
                        new_actives.add((test_x, test_y, test_z, test_w))

    active = new_actives

ANSWER2 = answer2(len(active))
