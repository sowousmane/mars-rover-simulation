import pytest

from mars_rover.simulation import Simulation


def test_simulation_runs_sample_input():
    lines = [
        "5 5",
        "1 2 N",
        "LMLMLMLMM",
        "3 3 E",
        "MMRMMRMRRM",
    ]

    simulation = Simulation.from_lines(lines)

    assert simulation.run() == ["1 3 N", "5 1 E"]


def test_simulation_with_invalid_plateau():
    lines = [
        "5",
        "1 2 N",
        "LMLMLMLMM",
    ]

    with pytest.raises(ValueError, match="plateau"):
        Simulation.from_lines(lines)


def test_simulation_with_invalid_command():
    lines = [
        "5 5",
        "1 2 N",
        "LMLX",
    ]

    with pytest.raises(ValueError, match="Commande invalide"):
        Simulation.from_lines(lines)
