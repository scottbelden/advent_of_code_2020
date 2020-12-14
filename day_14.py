from collections import Counter
from itertools import product
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_14_input")

memory = {}
for line in lines:
    if "mask" in line:
        mask_string = line.split(" = ")[1]

        and_mask = int(mask_string.replace("X", "1"), 2)
        or_mask = int(mask_string.replace("X", "0"), 2)
    else:
        mem_part, value = line.split(" = ")
        value = int(value)
        mem_address = int(mem_part[4:-1])

        memory[mem_address] = (value | or_mask) & and_mask

ANSWER1 = answer1(sum(memory.values()))

memory = {}
for line in lines:
    if "mask" in line:
        mask_string = line.split(" = ")[1]

        x_bits = [index for index, bit in enumerate(mask_string) if bit == "X"]
        num_x = Counter(mask_string)["X"]
        or_mask = int(mask_string.replace("X", "0"), 2)
    else:
        mem_part, value = line.split(" = ")
        value = int(value)
        mem_address = int(mem_part[4:-1])
        masked_mem_address = format(mem_address | or_mask, "036b")

        for bits in product("10", repeat=num_x):
            new_address = masked_mem_address
            for index, bit in zip(x_bits, bits):
                new_address = new_address[:index] + bit + new_address[index + 1 :]

            memory[int(new_address, 2)] = value

ANSWER2 = answer2(sum(memory.values()))
