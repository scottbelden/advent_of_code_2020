from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

seats = get_input("day_05_input")


def decode(encoded, first_row, last_row):
    encoded = encoded.replace("F", "0")
    encoded = encoded.replace("L", "0")
    encoded = encoded.replace("B", "1")
    encoded = encoded.replace("R", "1")

    return int(encoded, 2)


seat_ids = []
for seat in seats:
    encoded_row = seat[:7]
    encoded_column = seat[7:]

    seat_ids.append((decode(encoded_row, 0, 127) * 8) + decode(encoded_column, 0, 7))

ANSWER1 = answer1(max(seat_ids))

my_seat_id = None
for seat_id in range(min(seat_ids), max(seat_ids)):
    if seat_id not in seat_ids:
        my_seat_id = seat_id

ANSWER2 = answer2(my_seat_id)
