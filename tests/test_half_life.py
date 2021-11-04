from unittest.mock import MagicMock

import pytest

import half_life
from half_life.half_life import run_experiment


@pytest.mark.parametrize(
    "nr_die, nr_throws, expected",
    [
        (0, 0, [0]),
        (1, 1, [1, 1]),
        (3, 3, [3, 3, 3, 3]),
        (10, 10, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]),
    ],
)
def test_experiment(nr_die, nr_throws, expected, monkeypatch):
    result_mock = MagicMock()
    result_mock.roll.return_value = 1
    monkeypatch.setattr(
        half_life.half_life, "Dice", MagicMock(return_value=result_mock)
    )
    assert run_experiment(nr_die, nr_throws) == expected


@pytest.mark.parametrize(
    "nr_die, nr_throws, expected",
    [
        (0, 0, [0]),
        (1, 1, [1, 0]),
        (3, 3, [3, 0, 0, 0]),
    ],
)
def test_experiment_only_six(nr_die, nr_throws, expected, monkeypatch):
    result_mock = MagicMock()
    result_mock.roll.return_value = 6
    monkeypatch.setattr(
        half_life.half_life, "Dice", MagicMock(return_value=result_mock)
    )
    assert run_experiment(nr_die, nr_throws) == expected
