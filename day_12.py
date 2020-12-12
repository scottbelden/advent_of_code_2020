from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def process_instruction(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])

        if action == "N":
            self.y += value
        elif action == "S":
            self.y -= value
        elif action == "E":
            self.x += value
        elif action == "W":
            self.x -= value
        elif action == "L":
            self.direction += value
        elif action == "R":
            self.direction -= value
        elif action == "F":
            corrected_direction = self.direction % 360
            if corrected_direction == 0:
                self.x += value
            elif corrected_direction == 90:
                self.y += value
            elif corrected_direction == 180:
                self.x -= value
            elif corrected_direction == 270:
                self.y -= value
            else:
                raise Exception(f"Bad direction: {corrected_direction}")

    def get_distance(self):
        return abs(self.x) + abs(self.y)


directions = get_input("day_12_input")

ship = Ship()
for direction in directions:
    ship.process_instruction(direction)

ANSWER1 = answer1(ship.get_distance())


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_relative_x = 10
        self.waypoint_relative_y = 1
        self.direction = 0

    def process_instruction(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])

        current_waypoint_x = self.waypoint_relative_x
        current_waypoint_y = self.waypoint_relative_y

        if action == "N":
            self.waypoint_relative_y += value
        elif action == "S":
            self.waypoint_relative_y -= value
        elif action == "E":
            self.waypoint_relative_x += value
        elif action == "W":
            self.waypoint_relative_x -= value
        elif action == "L":
            if value == 90:
                self.waypoint_relative_x = -current_waypoint_y
                self.waypoint_relative_y = current_waypoint_x
            elif value == 180:
                self.waypoint_relative_x = -current_waypoint_x
                self.waypoint_relative_y = -current_waypoint_y
            elif value == 270:
                self.waypoint_relative_x = current_waypoint_y
                self.waypoint_relative_y = -current_waypoint_x
        elif action == "R":
            if value == 90:
                self.waypoint_relative_x = current_waypoint_y
                self.waypoint_relative_y = -current_waypoint_x
            elif value == 180:
                self.waypoint_relative_x = -current_waypoint_x
                self.waypoint_relative_y = -current_waypoint_y
            elif value == 270:
                self.waypoint_relative_x = -current_waypoint_y
                self.waypoint_relative_y = current_waypoint_x
        elif action == "F":
            self.x += self.waypoint_relative_x * value
            self.y += self.waypoint_relative_y * value

    def get_distance(self):
        return abs(self.x) + abs(self.y)


ship = Ship()
for direction in directions:
    ship.process_instruction(direction)

ANSWER2 = answer2(ship.get_distance())
