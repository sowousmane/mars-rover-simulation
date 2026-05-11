class Plateau:
    def __init__(self, max_x, max_y):
        if not isinstance(max_x, int) or not isinstance(max_y, int):
            raise ValueError("Les dimensions du plateau doivent etre des entiers.")

        if max_x < 0 or max_y < 0:
            raise ValueError("Les dimensions du plateau doivent etre positives ou nulles.")

        self.max_x = max_x
        self.max_y = max_y

    def contains(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
