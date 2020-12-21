DEBUG = False


def answer1(value):
    print(f"Part 1 Answer: {value}")
    return value


def answer2(value):
    print(f"Part 2 Answer: {value}")
    return value


def get_input(filename):
    with open(filename) as fp:
        return [line.strip() for line in fp]


def get_line_separated_inputs(filename):
    chunks = []
    chunk = []
    with open(filename) as fp:
        for line in fp:
            if line.strip() == "":
                chunks.append(chunk)
                chunk = []
            else:
                chunk.append(line.strip())

    if chunk:
        chunks.append(chunk)

    return chunks


def debug(string):
    if DEBUG:
        print(string)
