import re
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None


def passport_string_to_dict(passport_string):
    result = {}
    for item in passport_string.split():
        key, value = item.split(":")
        result[key] = value

    return result


passports = []
passport = ""
for line in get_input("day_04_input"):
    if line == "":
        passports.append(passport_string_to_dict(passport))
        passport = ""

    if passport == "":
        passport = line
    else:
        passport += " " + line

if passport:
    passports.append(passport_string_to_dict(passport))

valid_count = 0
for passport in passports:
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
        valid_count += 1

ANSWER1 = answer1(valid_count)

valid_count = 0
for passport in passports:
    birth_year = int(passport.get("byr", "0"))
    if birth_year < 1920 or birth_year > 2002:
        continue

    issue_year = int(passport.get("iyr", "0"))
    if issue_year < 2010 or issue_year > 2020:
        continue

    expiration_year = int(passport.get("eyr", "0"))
    if expiration_year < 2020 or expiration_year > 2030:
        continue

    height = passport.get("hgt", "0cm")
    height_value = height[:-2]
    if height_value == "":
        height_value = 0
    else:
        height_value = int(height_value)

    if "cm" in height:
        if height_value < 150 or height_value > 193:
            continue
    else:
        if height_value < 59 or height_value > 76:
            continue

    hair_color = passport.get("hcl", "#")
    if re.fullmatch(r"#[0-9a-f]{6}", hair_color) is None:
        continue

    eye_color = passport.get("ecl", "")
    if eye_color not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        continue

    pid = passport.get("pid", "")
    if re.fullmatch(r"[0-9]{9}", pid) is None:
        continue

    valid_count += 1

ANSWER2 = answer2(valid_count)
