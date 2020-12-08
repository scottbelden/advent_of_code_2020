from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

boot_code = get_input("day_08_input")


class InfiniteLoop(Exception):
    def __init__(self, accumulator):
        super().__init__("")
        self.accumulator = accumulator


def run_boot_code(boot_code):
    accumulator = 0
    instruction_pointer = 0
    instructions_visited = set()

    while True:
        if instruction_pointer in instructions_visited:
            raise InfiniteLoop(accumulator)

        if instruction_pointer >= len(boot_code):
            return accumulator

        instructions_visited.add(instruction_pointer)
        instruction, value = boot_code[instruction_pointer].split()

        if instruction == "nop":
            instruction_pointer += 1
        elif instruction == "acc":
            accumulator += int(value)
            instruction_pointer += 1
        elif instruction == "jmp":
            instruction_pointer += int(value)


try:
    run_boot_code(boot_code)
except InfiniteLoop as exc:
    ANSWER1 = answer1(exc.accumulator)

for index, line in enumerate(boot_code):
    if "nop" in line:
        test_code = [test_line for test_line in boot_code]
        test_code[index] = test_code[index].replace("nop", "jmp")
    elif "jmp" in line:
        test_code = [test_line for test_line in boot_code]
        test_code[index] = test_code[index].replace("jmp", "nop")
    else:
        continue

    try:
        final_value = run_boot_code(test_code)
    except InfiniteLoop:
        continue
    else:
        break

ANSWER2 = answer2(final_value)
