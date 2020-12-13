from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

timestamp, bus_string = get_input("day_13_input")

timestamp = int(timestamp)
busses = [int(bus) for bus in bus_string.split(",") if bus != "x"]

earliest = (float("inf"), None)
for bus in busses:
    missed_by = timestamp % bus
    if missed_by == 0:
        wait_time = 0
    else:
        wait_time = bus - missed_by

    if wait_time < earliest[0]:
        earliest = (wait_time, bus)

ANSWER1 = answer1(earliest[0] * earliest[1])

biggest_bus = max(busses)
index_of_biggest = bus_string.split(",").index(str(biggest_bus))

min_offset = None
others = []
for index, bus in enumerate(bus_string.split(",")):
    if bus == "x":
        continue

    if int(bus) == biggest_bus:
        continue

    others.append((int(bus), index - index_of_biggest))
    if min_offset is None:
        min_offset = index - index_of_biggest

factor = -1
current_time = biggest_bus
while True:
    for index, (other_bus, offset) in enumerate(others):
        if (current_time + offset) % other_bus == 0:
            if index > factor:
                factor = index
                biggest_bus = biggest_bus * other_bus
            continue
        else:
            break
    else:
        break

    current_time += biggest_bus

ANSWER2 = answer2(current_time + min_offset)
