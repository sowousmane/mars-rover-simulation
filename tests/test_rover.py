from mars_rover.plateau import Plateau
from mars_rover.rover import Rover


def build_rover(x=0, y=0, direction="N", max_x=5, max_y=5):
    plateau = Plateau(max_x, max_y)
    return Rover(x, y, direction, plateau)


def test_rover_turn_left():
    rover = build_rover(direction="N")
    assert rover.turn_left() == "W"

    rover.direction = "W"
    assert rover.turn_left() == "S"

    rover.direction = "S"
    assert rover.turn_left() == "E"

    rover.direction = "E"
    assert rover.turn_left() == "N"


def test_rover_turn_right():
    rover = build_rover(direction="N")
    assert rover.turn_right() == "E"

    rover.direction = "E"
    assert rover.turn_right() == "S"

    rover.direction = "S"
    assert rover.turn_right() == "W"

    rover.direction = "W"
    assert rover.turn_right() == "N"


def test_rover_move_north():
    rover = build_rover(x=1, y=1, direction="N")
    assert rover.move() == (1, 2)


def test_rover_move_out_of_bounds():
    rover = build_rover(x=5, y=5, direction="N")
    assert rover.move() == (5, 5)


def test_rover_execute_commands_stays_on_plateau_boundary():
    rover = build_rover(x=0, y=0, direction="W")
    assert rover.execute("M") == (0, 0, "W")


def test_rover_execute_commands():
    rover = build_rover(x=1, y=2, direction="N")
    assert rover.execute("LMLMLMLMM") == (1, 3, "N")
