def turn_left(direction):
    if direction == "N":
        return "W"
    elif direction == "W":
        return "S"
    elif direction == "S":
        return "E"
    elif direction == "E":
        return "N"
    else:
        raise ValueError(f"Invalid direction: {direction}")


def turn_right(direction):  
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        raise ValueError(f"Invalid direction: {direction}")

def is_inside(x, y, max_x, max_y):
    return 0 <= x <= max_x and 0 <= y <= max_y


def move(x, y, direction, max_x, max_y):
    new_x, new_y = x, y

    if direction == "N":
        new_y += 1
    elif direction == "S":
        new_y -= 1
    elif direction == "E":
        new_x += 1
    elif direction == "W":
        new_x -= 1

    if is_inside(new_x, new_y, max_x, max_y):
        return new_x, new_y

    return x, y

def execute_commands(x, y, direction, commands, max_x, max_y):
    for cmd in commands:
        if cmd == "L":
            direction = turn_left(direction)

        elif cmd == "R":
            direction = turn_right(direction)

        elif cmd == "M":
            x, y = move(x, y, direction, max_x, max_y)

        else:
            raise ValueError(f"Invalid command: {cmd}")

    return x, y, direction
