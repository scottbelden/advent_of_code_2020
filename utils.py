def answer1(value):
    print(f"Part 1 Answer: {value}")

def answer2(value):
    print(f"Part 2 Answer: {value}")

def get_input(filename):
    with open(filename) as fp:
        return [line.strip() for line in fp]
