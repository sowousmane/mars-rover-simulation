import logging

from rover import execute_commands


VALID_DIRECTIONS = {"N", "E", "S", "W"}
VALID_COMMANDS = {"L", "R", "M"}


def parse_plateau(line):
    parts = line.split()

    if len(parts) != 2:
        raise ValueError("Le plateau doit etre au format: max_x max_y")

    try:
        max_x = int(parts[0])
        max_y = int(parts[1])
    except ValueError as exc:
        raise ValueError("Les dimensions du plateau doivent etre des entiers.") from exc

    if max_x < 0 or max_y < 0:
        raise ValueError("Les dimensions du plateau doivent etre positives ou nulles.")

    return max_x, max_y


def parse_rover_position(line):
    parts = line.split()

    if len(parts) != 3:
        raise ValueError("La position du rover doit etre au format: x y direction")

    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError as exc:
        raise ValueError("Les coordonnees du rover doivent etre des entiers.") from exc

    direction = parts[2]
    if direction not in VALID_DIRECTIONS:
        raise ValueError(f"Direction invalide: {direction}")

    return x, y, direction


def validate_commands(commands):
    if not commands:
        raise ValueError("La ligne de commandes ne doit pas etre vide.")

    for command in commands:
        if command not in VALID_COMMANDS:
            raise ValueError(f"Commande invalide: {command}")

    return commands


def run_simulation(lines):
    if not lines:
        raise ValueError("Aucune donnee a simuler.")

    plateau_x, plateau_y = parse_plateau(lines[0])
    logging.info("Plateau detecte: %s %s", plateau_x, plateau_y)

    if (len(lines) - 1) % 2 != 0:
        raise ValueError("Chaque rover doit avoir une ligne position et une ligne commandes.")

    results = []
    i = 1

    while i < len(lines):
        x, y, direction = parse_rover_position(lines[i])
        commands = validate_commands(lines[i + 1])

        if x < 0 or y < 0 or x > plateau_x or y > plateau_y:
            raise ValueError("La position initiale du rover est en dehors du plateau.")

        logging.info("Rover initial: %s %s %s", x, y, direction)
        logging.info("Commandes: %s", commands)

        x, y, direction = execute_commands(
            x, y,
            direction,
            commands,
            plateau_x,
            plateau_y
        )

        logging.info("Position finale: %s %s %s", x, y, direction)
        results.append(f"{x} {y} {direction}")

        i += 2

    return results
