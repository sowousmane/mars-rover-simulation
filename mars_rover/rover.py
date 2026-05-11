import logging


class Rover:
    DIRECTIONS = ["N", "E", "S", "W"]
    MOVEMENTS = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    def __init__(self, x, y, direction, plateau):
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Direction invalide: {direction}")

        if not plateau.contains(x, y):
            raise ValueError("La position initiale du rover est en dehors du plateau.")

        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau

    def turn_left(self):
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index - 1) % len(self.DIRECTIONS)]
        return self.direction

    def turn_right(self):
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % len(self.DIRECTIONS)]
        return self.direction

    def move(self):
        delta_x, delta_y = self.MOVEMENTS[self.direction]
        new_x = self.x + delta_x
        new_y = self.y + delta_y

        if self.plateau.contains(new_x, new_y):
            logging.info(
                "Mouvement applique: (%s, %s) -> (%s, %s)",
                self.x, self.y, new_x, new_y
            )
            self.x = new_x
            self.y = new_y
        else:
            logging.info(
                "Mouvement bloque par la limite du plateau: (%s, %s) reste inchange",
                self.x, self.y
            )

        return self.x, self.y

    def execute(self, commands):
        for command in commands:
            logging.info("Commande en cours: %s", command)

            if command == "L":
                old_direction = self.direction
                self.turn_left()
                logging.info("Rotation gauche: %s -> %s", old_direction, self.direction)
            elif command == "R":
                old_direction = self.direction
                self.turn_right()
                logging.info("Rotation droite: %s -> %s", old_direction, self.direction)
            elif command == "M":
                logging.info(
                    "Tentative de mouvement depuis (%s, %s) vers %s",
                    self.x, self.y, self.direction
                )
                self.move()
            else:
                raise ValueError(f"Commande invalide: {command}")

        return self.position()

    def position(self):
        return self.x, self.y, self.direction

    def __str__(self):
        return f"{self.x} {self.y} {self.direction}"
