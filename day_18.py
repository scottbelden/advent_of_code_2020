from io import StringIO
from operator import add, mul
from string import digits
import re

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_18_input")


def evaluate_line(chars):
    total = None
    op = None

    while char := chars.read(1):
        if char == "*":
            op = mul
            continue
        elif char == "+":
            op = add
            continue
        elif char == "(":
            numeral = evaluate_line(chars)
        elif char == ")":
            return total
        else:
            numeral = int(char)

        if op:
            total = op(total, numeral)
        else:
            total = numeral

    return total


total = 0
for line in lines:
    compact = line.replace(" ", "")
    total += evaluate_line(StringIO(compact))

ANSWER1 = answer1(total)


def get_int(chars):
    loc = chars.tell()
    char = chars.read(1)
    if char in digits:
        return char
    else:
        chars.seek(loc)


def evaluate_line(chars):
    total = None
    op = None

    while char := chars.read(1):
        if char == "*":
            op = mul
            numeral = evaluate_line(chars)
        elif char == "+":
            op = add
            continue
        else:
            number_string = char
            while next_int := get_int(chars):
                number_string += next_int
            numeral = int(number_string)

        if op:
            total = op(total, numeral)
        else:
            total = numeral

    return total


total = 0
for line in lines:
    compact = line.replace(" ", "")
    while m := re.search(r"\([+*0-9]*?\)", compact):
        value = evaluate_line(StringIO(m.group()[1:-1]))
        compact = compact.replace(m.group(), str(value))

    total += evaluate_line(StringIO(compact))

ANSWER2 = answer2(total)
