from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

values = [int(line) for line in get_input("day_01_input")]

for index, value in enumerate(values):
    for value2 in values[index + 1 :]:
        if value + value2 == 2020:
            ANSWER1 = answer1(value * value2)

for index, value in enumerate(values):
    for index2, value2 in enumerate(values[index + 1 :]):
        for value3 in values[index2 + index :]:
            if value + value2 + value3 == 2020:
                ANSWER2 = answer2(value * value2 * value3)
