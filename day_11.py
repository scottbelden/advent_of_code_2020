from collections import Counter

from utils import answer1, answer2, get_input, debug

ANSWER1 = None
ANSWER2 = None

seats = get_input("day_11_input")

debug("Original")
for row in seats:
    debug(row)

iteration = 0
while True:
    debug("")
    debug(f"{iteration=}")
    new_seats = []
    for y_index, row in enumerate(seats):
        new_row = ""
        for x_index, char in enumerate(row):
            if char == ".":
                new_row += "."
                continue

            is_left_column = x_index == 0
            is_right_column = x_index == len(row) - 1
            is_top_row = y_index == 0
            is_bottom_row = y_index == len(seats) - 1
            num_adjacent = 0

            # Check Right
            num_adjacent += not is_right_column and seats[y_index][x_index + 1] == "#"
            # Check Bottom Right
            num_adjacent += (
                not is_right_column
                and not is_bottom_row
                and seats[y_index + 1][x_index + 1] == "#"
            )
            # Check Bottom
            num_adjacent += not is_bottom_row and seats[y_index + 1][x_index] == "#"
            # Check Bottom Left
            num_adjacent += (
                not is_bottom_row
                and not is_left_column
                and seats[y_index + 1][x_index - 1] == "#"
            )
            # Check Left
            num_adjacent += not is_left_column and seats[y_index][x_index - 1] == "#"
            # Check Top Left
            num_adjacent += (
                not is_top_row
                and not is_left_column
                and seats[y_index - 1][x_index - 1] == "#"
            )
            # Check Top
            num_adjacent += not is_top_row and seats[y_index - 1][x_index] == "#"
            # Check Top Right
            num_adjacent += (
                not is_top_row
                and not is_right_column
                and seats[y_index - 1][x_index + 1] == "#"
            )

            if char == "L" and num_adjacent == 0:
                new_row += "#"
            elif char == "#" and num_adjacent >= 4:
                new_row += "L"
            else:
                new_row += char

        new_seats.append(new_row)

    for row in new_seats:
        debug(row)

    if seats == new_seats:
        break
    else:
        seats = new_seats
        iteration += 1

total_occupied = sum([Counter(row)["#"] for row in seats])

ANSWER1 = answer1(total_occupied)

seats = get_input("day_11_input")


def is_occupied(chars):
    for char in chars:
        if char == ".":
            continue
        elif char == "#":
            return True
        elif char == "L":
            return False

    return False


debug("Original")
for row in seats:
    debug(row)

iteration = 0
while True:
    debug("")
    debug(f"{iteration=}")
    new_seats = []
    for y_index, row in enumerate(seats):
        new_row = ""
        for x_index, char in enumerate(row):
            if char == ".":
                new_row += "."
                continue

            is_left_column = x_index == 0
            is_right_column = x_index == len(row) - 1
            is_top_row = y_index == 0
            is_bottom_row = y_index == len(seats) - 1
            num_adjacent = 0

            # Check Right
            num_adjacent += not is_right_column and is_occupied(
                seats[y_index][x_index + 1 :]
            )
            # Check Bottom Right
            distance_to_edge = min(len(seats) - 1 - y_index, len(row) - 1 - x_index)
            num_adjacent += (
                not is_bottom_row
                and not is_right_column
                and is_occupied(
                    c
                    for z in range(1, distance_to_edge + 1)
                    for c in seats[y_index + z][x_index + z]
                )
            )
            # Check Bottom
            num_adjacent += not is_bottom_row and is_occupied(
                c
                for z in range(1, len(seats) - y_index)
                for c in seats[y_index + z][x_index]
            )
            # Check Bottom Left
            distance_to_edge = min(len(seats) - 1 - y_index, x_index)
            num_adjacent += (
                not is_bottom_row
                and not is_left_column
                and is_occupied(
                    c
                    for z in range(1, distance_to_edge + 1)
                    for c in seats[y_index + z][x_index - z]
                )
            )
            # Check Left
            num_adjacent += not is_left_column and is_occupied(
                seats[y_index][:x_index][::-1]
            )
            # Check Top Left
            distance_to_edge = min(y_index, x_index)
            num_adjacent += (
                not is_top_row
                and not is_left_column
                and is_occupied(
                    c
                    for z in range(1, distance_to_edge + 1)
                    for c in seats[y_index - z][x_index - z]
                )
            )
            # Check Top
            num_adjacent += not is_top_row and is_occupied(
                c for z in range(1, y_index + 1) for c in seats[y_index - z][x_index]
            )
            # Check Top Right
            distance_to_edge = min(y_index, len(row) - 1 - x_index)
            num_adjacent += (
                not is_top_row
                and not is_right_column
                and is_occupied(
                    c
                    for z in range(1, distance_to_edge + 1)
                    for c in seats[y_index - z][x_index + z]
                )
            )

            if char == "L" and num_adjacent == 0:
                new_row += "#"
            elif char == "#" and num_adjacent >= 5:
                new_row += "L"
            else:
                new_row += char

        new_seats.append(new_row)

    for row in new_seats:
        debug(row)

    if seats == new_seats:
        break
    else:
        seats = new_seats
        iteration += 1

total_occupied = sum([Counter(row)["#"] for row in seats])

ANSWER2 = answer2(total_occupied)
