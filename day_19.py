import regex

from utils import answer1, answer2, get_line_separated_inputs

ANSWER1 = None
ANSWER2 = None

rules, test_cases = get_line_separated_inputs("day_19_input")

patterns = {}
rule_map = {}
for rule in rules:
    index, right_side = rule.split(": ")
    if right_side == '"a"':
        patterns[index] = "a"
    elif right_side == '"b"':
        patterns[index] = "b"
    else:
        ors = right_side.split(" | ")
        rule_map[index] = [or_.split() for or_ in ors]

while True:
    for index, list_of_groups in rule_map.items():
        defined_patterns = set(patterns)

        can_resolve = True
        for group in list_of_groups:
            if set(group) != set(group) & defined_patterns:
                can_resolve = False
                break

        if can_resolve:
            resolved_groups = []
            for group in list_of_groups:
                resolved_groups.append("".join(patterns[item] for item in group))

            pattern = "((" + ")|(".join(resolved_groups) + "))"
            break

    del rule_map[index]
    patterns[index] = pattern

    if len(rule_map) == 0:
        break

total = 0
compiled = regex.compile(patterns["0"])
for test_case in test_cases:
    if regex.fullmatch(compiled, test_case):
        total += 1

ANSWER1 = answer1(total)


patterns = {}
rule_map = {}
for rule in rules:
    index, right_side = rule.split(": ")
    if index == "8":
        right_side = "42 | 42 8"
    elif index == "11":
        right_side = "42 31 | 42 11 31"

    if right_side == '"a"':
        patterns[index] = "a"
    elif right_side == '"b"':
        patterns[index] = "b"
    else:
        ors = right_side.split(" | ")
        rule_map[index] = [or_.split() for or_ in ors]

while True:
    for index, list_of_groups in rule_map.items():
        defined_patterns = set(patterns)

        can_resolve = True
        for group in list_of_groups:
            if set(group) - set([index]) != set(group) & defined_patterns:
                can_resolve = False
                break

        if can_resolve:
            if index == "8":
                pattern = "(" + patterns["42"] + "+)"
            elif index == "11":
                pattern = "(" + patterns["42"] + "(?R)?" + patterns["31"] + ")"
                pattern = (
                    "("
                    + patterns["42"]
                    + "("
                    + patterns["42"]
                    + "("
                    + patterns["42"]
                    + "("
                    + patterns["42"]
                    + "("
                    + patterns["42"]
                    + patterns["31"]
                    + ")*"
                    + patterns["31"]
                    + ")*"
                    + patterns["31"]
                    + ")*"
                    + patterns["31"]
                    + ")*"
                    + patterns["31"]
                    + ")"
                )
            else:
                resolved_groups = []
                for group in list_of_groups:
                    resolved_groups.append("".join(patterns[item] for item in group))

                pattern = "((" + ")|(".join(resolved_groups) + "))"
            break
    else:
        raise Exception()
    del rule_map[index]
    patterns[index] = pattern

    if len(rule_map) == 0:
        break

total = 0
compiled = regex.compile(patterns["0"])
for test_case in test_cases:
    if regex.fullmatch(compiled, test_case):
        total += 1

ANSWER2 = answer2(total)
