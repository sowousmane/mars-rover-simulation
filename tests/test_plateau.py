import pytest

from mars_rover.plateau import Plateau


def test_plateau_contains_position_inside():
    plateau = Plateau(5, 5)
    assert plateau.contains(3, 4) is True


def test_plateau_rejects_negative_dimensions():
    with pytest.raises(ValueError, match="positives ou nulles"):
        Plateau(-1, 5)
