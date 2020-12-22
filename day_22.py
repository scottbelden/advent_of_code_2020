from collections import deque

from utils import answer1, answer2, get_line_separated_inputs

ANSWER1 = None
ANSWER2 = None

player1, player2 = get_line_separated_inputs("day_22_input")

p1_hand = deque([int(card) for card in player1[1:]])
p2_hand = deque([int(card) for card in player2[1:]])

while len(p1_hand) > 0 and len(p2_hand) > 0:
    if p1_hand[0] > p2_hand[0]:
        p1_hand.rotate(-1)
        p1_hand.append(p2_hand.popleft())
    elif p2_hand[0] > p1_hand[0]:
        p2_hand.rotate(-1)
        p2_hand.append(p1_hand.popleft())
    else:
        breakpoint()
        raise Exception()

    # print(f"{p1_hand=}")
    # print(f"{p2_hand=}")

winner = p1_hand if len(p1_hand) > 0 else p2_hand
winner.reverse()

score = 0
for index, card in enumerate(winner):
    score += card * (index + 1)

ANSWER1 = answer1(score)

game_count = 1


def recursive_combat(p1_hand, p2_hand, game_number):
    previous_hands = []
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        winner = None
        if (p1_hand, p2_hand) in previous_hands:
            # Player 1 wins
            return "player1", p1_hand
        else:
            previous_hands.append((p1_hand.copy(), p2_hand.copy()))

        if (p1_hand[0] <= (len(p1_hand) - 1)) and (p2_hand[0] <= (len(p2_hand) - 1)):
            p1_copy = p1_hand.copy()
            p2_copy = p2_hand.copy()
            for new_hand in (p1_copy, p2_copy):
                max_length = new_hand.popleft()
                while len(new_hand) > max_length:
                    new_hand.pop()

            global game_count
            game_count += 1
            winner, _ = recursive_combat(p1_copy, p2_copy, game_count)

        elif p1_hand[0] > p2_hand[0]:
            winner = "player1"
        elif p2_hand[0] > p1_hand[0]:
            winner = "player2"
        else:
            raise Exception()

        if winner == "player1":
            p1_hand.rotate(-1)
            p1_hand.append(p2_hand.popleft())
        elif winner == "player2":
            p2_hand.rotate(-1)
            p2_hand.append(p1_hand.popleft())
        else:
            raise Exception()

    if len(p1_hand) == 0:
        return "player2", p2_hand
    else:
        return "player1", p1_hand


p1_hand = deque([int(card) for card in player1[1:]])
p2_hand = deque([int(card) for card in player2[1:]])

_, winner_hand = recursive_combat(p1_hand, p2_hand, 1)

winner_hand.reverse()

score = 0
for index, card in enumerate(winner_hand):
    score += card * (index + 1)

ANSWER2 = answer2(score)
