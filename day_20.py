from collections import defaultdict, Counter
from dataclasses import dataclass

from utils import answer1, answer2, get_line_separated_inputs

ANSWER1 = None
ANSWER2 = None


@dataclass
class Tile:
    id: int
    lines: list[str]

    def __str__(self):
        ret = ""
        ret += f"Tile: {self.id}\n"
        for line in self.lines:
            ret += f"{line}\n"
        return ret

    def __post_init__(self):
        self.top = self.lines[0]
        self.bottom = self.lines[-1]
        self.left = "".join(line[0] for line in self.lines)
        self.right = "".join(line[-1] for line in self.lines)

        sides = [
            set([self.top, self.top[::-1]]),
            set([self.bottom, self.bottom[::-1]]),
            set([self.left, self.left[::-1]]),
            set([self.right, self.right[::-1]]),
        ]
        self.sides = sides
        self.top_neighbor = None
        self.bottom_neighbor = None
        self.left_neighbor = None
        self.right_neighbor = None

    def flip(self):
        self.left, self.right = self.right, self.left
        self.top = self.top[::-1]
        self.bottom = self.bottom[::-1]

        self.left_neighbor, self.right_neighbor = (
            self.right_neighbor,
            self.left_neighbor,
        )

        self.lines = [line[::-1] for line in self.lines]

    def rotate_cw(self):
        current_right = self.right
        self.right = self.top
        self.top = self.left[::-1]
        self.left = self.bottom
        self.bottom = current_right[::-1]

        (
            self.top_neighbor,
            self.right_neighbor,
            self.bottom_neighbor,
            self.left_neighbor,
        ) = (
            self.left_neighbor,
            self.top_neighbor,
            self.right_neighbor,
            self.bottom_neighbor,
        )

        rotated_lines = []
        for i in range(len(self.lines)):
            new_line = ""
            for line in self.lines[::-1]:
                new_line += line[i]
            rotated_lines.append(new_line)
        self.lines = rotated_lines


input_tiles = get_line_separated_inputs("day_20_input")

all_tiles = {}
tiles = []
for tile in input_tiles:
    tile_id = int(tile[0].split()[1][:-1])
    new_tile = Tile(tile_id, tile[1:])
    tiles.append(new_tile)
    all_tiles[tile_id] = new_tile

tile_length = len(new_tile.top)

corner_tile = None
tile_neighbors = defaultdict(set)
total = 1
for tile in tiles:
    for other_tile in tiles:
        if tile.id == other_tile.id:
            continue

        for side in tile.sides:
            for other_side in other_tile.sides:
                if side == other_side:
                    tile_neighbors[tile.id].add(other_tile.id)
                    if tile.top in side:
                        tile.top_neighbor = other_tile.id
                    elif tile.bottom in side:
                        tile.bottom_neighbor = other_tile.id
                    elif tile.left in side:
                        tile.left_neighbor = other_tile.id
                    elif tile.right in side:
                        tile.right_neighbor = other_tile.id

    if len(tile_neighbors[tile.id]) == 2:
        total *= tile.id
        corner_tile = tile

ANSWER1 = answer1(total)

if corner_tile.bottom_neighbor and corner_tile.left_neighbor:
    corner_tile.flip()
elif corner_tile.top_neighbor and corner_tile.left_neighbor:
    corner_tile.rotate_cw()
    corner_tile.rotate_cw()
elif corner_tile.top_neighbor and corner_tile.right_neighbor:
    corner_tile.rotate_cw()

big_map = [[corner_tile]]
current_line = 0
while True:
    current_tile = big_map[current_line][-1]
    right_tile = all_tiles[current_tile.right_neighbor]

    if right_tile.right_neighbor == current_tile.id:
        right_tile.flip()
    elif right_tile.top_neighbor == current_tile.id:
        right_tile.rotate_cw()
        right_tile.flip()
    elif right_tile.bottom_neighbor == current_tile.id:
        right_tile.rotate_cw()

    if current_tile.right != right_tile.left:
        right_tile.rotate_cw()
        right_tile.rotate_cw()
        right_tile.flip()

    big_map[current_line].append(right_tile)

    if right_tile.right_neighbor is None and right_tile.bottom_neighbor is None:
        break
    elif right_tile.right_neighbor is None:
        next_row_tile = all_tiles[big_map[current_line][0].bottom_neighbor]

        if next_row_tile.right_neighbor == big_map[current_line][0].id:
            next_row_tile.flip()
            next_row_tile.rotate_cw()
        elif next_row_tile.bottom_neighbor == big_map[current_line][0].id:
            next_row_tile.rotate_cw()
            next_row_tile.rotate_cw()
        elif next_row_tile.left_neighbor == big_map[current_line][0].id:
            next_row_tile.rotate_cw()

        if next_row_tile.left_neighbor is not None:
            next_row_tile.flip()

        big_map.append([next_row_tile])
        current_line += 1

full_map = []
for row in big_map:
    for i in range(tile_length):
        line = ""
        if i == 0 or i == (tile_length - 1):
            continue

        for tile in row:
            line += tile.lines[i][1:-1]

        full_map.append(line)

width = len(full_map[0])
height = len(full_map)
sea_monster_width = 20
found_monsters = 0
for flips in range(2):
    for rotations in range(4):
        for y_index, line in enumerate(full_map):
            if (y_index == height - 1) or (y_index == height - 2):
                # Don't look on last two lines
                continue

            for x_index in range(width):
                if x_index + sea_monster_width == width:
                    break

                # Look for sea monsters
                if (
                    full_map[y_index][x_index + 18] == "#"
                    and full_map[y_index + 1][x_index] == "#"
                    and full_map[y_index + 1][x_index + 5] == "#"
                    and full_map[y_index + 1][x_index + 6] == "#"
                    and full_map[y_index + 1][x_index + 11] == "#"
                    and full_map[y_index + 1][x_index + 12] == "#"
                    and full_map[y_index + 1][x_index + 17] == "#"
                    and full_map[y_index + 1][x_index + 18] == "#"
                    and full_map[y_index + 1][x_index + 19] == "#"
                    and full_map[y_index + 2][x_index + 1] == "#"
                    and full_map[y_index + 2][x_index + 4] == "#"
                    and full_map[y_index + 2][x_index + 7] == "#"
                    and full_map[y_index + 2][x_index + 10] == "#"
                    and full_map[y_index + 2][x_index + 13] == "#"
                    and full_map[y_index + 2][x_index + 16] == "#"
                ):
                    found_monsters += 1

        if found_monsters:
            break
        else:
            # Rotate
            rotated_lines = []
            for i in range(height):
                new_line = ""
                for line in full_map[::-1]:
                    new_line += line[i]
                rotated_lines.append(new_line)
            full_map = rotated_lines

    if found_monsters:
        break
    else:
        # Flip
        full_map = [line[::-1] for line in full_map]

hashes = sum(Counter(line)["#"] for line in full_map)

ANSWER2 = answer2(hashes - (15 * found_monsters))
