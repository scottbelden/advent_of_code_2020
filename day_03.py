from utils import answer1, answer2, get_input

area_map = get_input("day_03_input")
width = len(area_map[0])

def trees_hit(right, down):
    current_row = 0
    current_col = 0
    trees = 0

    while True:
        # Move
        current_row += down
        current_col += right

        if current_row + 1 > len(area_map):
            break

        char = area_map[current_row][current_col % width]
        if char == "#":
            trees += 1

    return trees

answer1(trees_hit(3, 1))

answer2(
    trees_hit(1, 1)
    * trees_hit(3, 1)
    * trees_hit(5, 1)
    * trees_hit(7, 1)
    * trees_hit(1, 2)
)