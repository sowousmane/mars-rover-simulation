from rover import turn_left, turn_right, move, execute_commands

def test_turn_left():
    assert turn_left("N") == "W"
    assert turn_left("W") == "S"
    assert turn_left("S") == "E"
    assert turn_left("E") == "N"

def test_turn_right():
    assert turn_right("N") == "E"
    assert turn_right("E") == "S"
    assert turn_right("S") == "W"
    assert turn_right("W") == "N"

def test_move_north():
    x, y = move(1, 1, "N", 5, 5)
    assert (x, y) == (1, 2)

def test_move_out_of_bounds():
    x, y = move(5, 5, "N", 5, 5)
    assert (x, y) == (5, 5)  # bloqué   

def test_execute_commands():
    x, y, direction = execute_commands(
        1, 2, "N", "LMLMLMLMM", 5, 5
    )

    assert (x, y, direction) == (1, 3, "N")
