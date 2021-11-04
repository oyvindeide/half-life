import pytest

from half_life.dice import Dice


@pytest.mark.parametrize("_", range(100))
def test_dice(_):
    die = Dice()
    assert 1 <= die.value <= 6


@pytest.mark.parametrize("_", range(100))
def test_die_roll(_):
    die = Dice()
    assert 1 <= die.roll() <= 6


def test_die_boundary():
    dice = [Dice() for _ in range(10000)]
    dice_values = [die.roll() for die in dice]
    assert 1 in dice_values and 6 in dice_values
