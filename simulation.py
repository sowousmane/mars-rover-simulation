from rover import execute_commands


def run_simulation(lines):
    plateau_x, plateau_y = map(int, lines[0].split())

    results = []
    i = 1

    while i < len(lines):
        x, y, direction = lines[i].split()
        x = int(x)
        y = int(y)

        commands = lines[i + 1]

        x, y, direction = execute_commands(
            x, y,
            direction,
            commands,
            plateau_x,
            plateau_y
        )

        results.append(f"{x} {y} {direction}")

        i += 2

    return results
