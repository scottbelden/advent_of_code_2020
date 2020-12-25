from utils import answer1, get_input_as_int

ANSWER1 = None

card_pk, door_pk = get_input_as_int("day_25_input")
card_loop = None
door_loop = None

subject_number = 7


def do_loop(current_value, subject_number, loop_size):
    for _ in range(loop_size):
        current_value *= subject_number
        current_value %= 20201227

    return current_value


for pk in (card_pk, door_pk):
    current_value = 1
    loop_size = 0
    while True:
        loop_size += 1
        current_value = do_loop(current_value, 7, 1)

        if current_value == pk:
            break

    if pk == card_pk:
        card_loop = loop_size
    else:
        door_loop = loop_size


encryption_key1 = do_loop(1, door_pk, card_loop)
encryption_key2 = do_loop(1, card_pk, door_loop)
assert encryption_key1 == encryption_key2

ANSWER1 = answer1(encryption_key1)
