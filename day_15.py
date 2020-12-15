from collections import deque, defaultdict

from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

starting_nums = get_input("day_15_input")[0].split(",")

history = defaultdict(lambda: deque(maxlen=2))
last_spoken = None
turn = 0
for num in starting_nums:
    turn += 1
    history[int(num)].append(turn)
    last_spoken = int(num)

while turn < 2020:
    turn += 1
    if len(history[last_spoken]) == 1:
        last_spoken = 0
        history[last_spoken].append(turn)
    else:
        last_spoken = history[last_spoken][1] - history[last_spoken][0]
        history[last_spoken].append(turn)

ANSWER1 = answer1(last_spoken)

history = defaultdict(lambda: deque(maxlen=2))
last_spoken = None
turn = 0
for num in starting_nums:
    turn += 1
    history[int(num)].append(turn)
    last_spoken = int(num)

while turn < 30000000:
    turn += 1
    if len(history[last_spoken]) == 1:
        last_spoken = 0
        history[last_spoken].append(turn)
    else:
        last_spoken = history[last_spoken][1] - history[last_spoken][0]
        history[last_spoken].append(turn)

ANSWER2 = answer2(last_spoken)
