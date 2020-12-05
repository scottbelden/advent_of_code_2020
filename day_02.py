from collections import Counter
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

valid_count = 0
for line in get_input("day_02_input"):
    char_range, char, password = line.split()
    min_count = int(char_range.split("-")[0])
    max_count = int(char_range.split("-")[1])
    char = char[0]

    if min_count <= Counter(password)[char] <= max_count:
        valid_count += 1

ANSWER1 = answer1(valid_count)

valid_count = 0
for line in get_input("day_02_input"):
    char_indexes, char, password = line.split()
    index_one = int(char_indexes.split("-")[0]) - 1
    index_two = int(char_indexes.split("-")[1]) - 1
    char = char[0]

    if (password[index_one] == char and password[index_two] != char) or (
        password[index_one] != char and password[index_two] == char
    ):
        valid_count += 1

ANSWER2 = answer2(valid_count)
