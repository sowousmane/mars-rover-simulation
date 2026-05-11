import logging

from mars_rover.plateau import Plateau
from mars_rover.rover import Rover


class Simulation:
    VALID_COMMANDS = {"L", "R", "M"}

    def __init__(self, plateau):
        self.plateau = plateau
        self.rover_jobs = []

    @classmethod
    def from_lines(cls, lines):
        if not lines:
            raise ValueError("Aucune donnee a simuler.")

        plateau = cls.parse_plateau(lines[0])
        logging.info("Plateau detecte: %s %s", plateau.max_x, plateau.max_y)

        if (len(lines) - 1) % 2 != 0:
            raise ValueError("Chaque rover doit avoir une ligne position et une ligne commandes.")

        simulation = cls(plateau)
        index = 1

        while index < len(lines):
            rover = cls.parse_rover(lines[index], plateau)
            commands = cls.validate_commands(lines[index + 1])
            simulation.add_rover(rover, commands)
            index += 2

        return simulation

    @staticmethod
    def parse_plateau(line):
        parts = line.split()

        if len(parts) != 2:
            raise ValueError("Le plateau doit etre au format: max_x max_y")

        try:
            max_x = int(parts[0])
            max_y = int(parts[1])
        except ValueError as exc:
            raise ValueError("Les dimensions du plateau doivent etre des entiers.") from exc

        return Plateau(max_x, max_y)

    @classmethod
    def parse_rover(cls, line, plateau):
        parts = line.split()

        if len(parts) != 3:
            raise ValueError("La position du rover doit etre au format: x y direction")

        try:
            x = int(parts[0])
            y = int(parts[1])
        except ValueError as exc:
            raise ValueError("Les coordonnees du rover doivent etre des entiers.") from exc

        direction = parts[2]
        return Rover(x, y, direction, plateau)

    @classmethod
    def validate_commands(cls, commands):
        if not commands:
            raise ValueError("La ligne de commandes ne doit pas etre vide.")

        for command in commands:
            if command not in cls.VALID_COMMANDS:
                raise ValueError(f"Commande invalide: {command}")

        return commands

    def add_rover(self, rover, commands):
        self.rover_jobs.append((rover, commands))

    def run(self):
        results = []

        for rover, commands in self.rover_jobs:
            logging.info("Rover initial: %s %s %s", rover.x, rover.y, rover.direction)
            logging.info("Commandes: %s", commands)
            rover.execute(commands)
            logging.info("Position finale: %s %s %s", rover.x, rover.y, rover.direction)
            results.append(str(rover))

        return results
