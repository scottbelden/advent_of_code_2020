from collections import defaultdict
from io import StringIO

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

directions = get_input("day_24_input")


def move(current_pos, direction):
    x, y = current_pos
    if direction == "e":
        return (x + 2, y)
    elif direction == "w":
        return (x - 2, y)
    elif direction == "nw":
        return (x - 1, y - 1)
    elif direction == "ne":
        return (x + 1, y - 1)
    elif direction == "sw":
        return (x - 1, y + 1)
    elif direction == "se":
        return (x + 1, y + 1)
    else:
        raise Exception()


# White is 0, black is 1
tiles = defaultdict(int)
for direction in directions:
    current_pos = (3, 3)
    dir_string = StringIO(direction)
    full_path = ""
    while char := dir_string.read(1):
        if char == "n" or char == "s":
            current_pos = move(current_pos, char + dir_string.read(1))
        else:
            current_pos = move(current_pos, char)

    tiles[current_pos] = (tiles[current_pos] + 1) % 2

ANSWER1 = answer1(sum(tiles.values()))

black_tiles = set(tile for tile, value in tiles.items() if value == 1)


def get_black_neighbors(tile, black_tiles):
    x, y = tile
    return sum(
        [
            (x + 2, y) in black_tiles,
            (x - 2, y) in black_tiles,
            (x - 1, y - 1) in black_tiles,
            (x + 1, y - 1) in black_tiles,
            (x - 1, y + 1) in black_tiles,
            (x + 1, y + 1) in black_tiles,
        ],
    )


def should_stay_black(black_tile, black_tiles):
    black_neighbors = get_black_neighbors(black_tile, black_tiles)
    if black_neighbors == 1 or black_neighbors == 2:
        return True
    else:
        return False


def should_flip_to_black(white_tile, black_tiles):
    black_neighbors = get_black_neighbors(white_tile, black_tiles)
    if black_neighbors == 2:
        return True
    else:
        return False


for night in range(100):
    new_black_tiles = set()
    white_tiles_to_check = set()
    for black_tile in black_tiles:
        black_x, black_y = black_tile
        to_check = set(
            [
                (black_x + 2, black_y),
                (black_x - 2, black_y),
                (black_x - 1, black_y - 1),
                (black_x + 1, black_y - 1),
                (black_x - 1, black_y + 1),
                (black_x + 1, black_y + 1),
            ],
        )
        white_tiles_to_check |= to_check
        if should_stay_black(black_tile, black_tiles):
            new_black_tiles.add(black_tile)

    for white_tile in white_tiles_to_check:
        if should_flip_to_black(white_tile, black_tiles):
            new_black_tiles.add(white_tile)

    black_tiles = new_black_tiles

ANSWER2 = answer2(len(black_tiles))
