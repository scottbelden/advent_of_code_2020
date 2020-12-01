from utils import answer1, answer2

values = []
with open("day_01_input") as fp:
    for line in fp:
        values.append(int(line.strip()))

for index, value in enumerate(values):
    for value2 in values[index + 1:]:
        if value + value2 == 2020:
            answer1(value * value2)

for index, value in enumerate(values):
    for index2, value2 in enumerate(values[index + 1:]):
        for value3 in values[index2 + index:]:
            if value + value2 + value3 == 2020:
                answer2(value * value2 * value3)
