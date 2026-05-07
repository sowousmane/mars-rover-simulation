import logging


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
    else:
        raise ValueError(f"Invalid direction: {direction}")

    if is_inside(new_x, new_y, max_x, max_y):
        logging.info(
            "Mouvement applique: (%s, %s) -> (%s, %s)",
            x, y, new_x, new_y
        )
        return new_x, new_y

    logging.info(
        "Mouvement bloque par la limite du plateau: (%s, %s) reste inchange",
        x, y
    )
    return x, y



def execute_commands(x, y, direction, commands, max_x, max_y):
    for cmd in commands:
        logging.info("Commande en cours: %s", cmd)

        if cmd == "L":
            old_direction = direction
            direction = turn_left(direction)
            logging.info(
                "Rotation gauche: %s -> %s",
                old_direction, direction
            )

        elif cmd == "R":
            old_direction = direction
            direction = turn_right(direction)
            logging.info(
                "Rotation droite: %s -> %s",
                old_direction, direction
            )

        elif cmd == "M":
            logging.info(
                "Tentative de mouvement depuis (%s, %s) vers %s",
                x, y, direction
            )
            x, y = move(x, y, direction, max_x, max_y)

        else:
            raise ValueError(f"Invalid command: {cmd}")

    return x, y, direction
