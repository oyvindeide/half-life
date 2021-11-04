from half_life.dice import Dice


def run_experiment(nr_of_dice, nr_throws):
    dice = [Dice() for _ in range(nr_of_dice)]

    nr_remaining = [len(dice)]

    for _ in range(nr_throws):
        values = [die.roll() for die in dice]
        nr_not_six = len([val for val in values if val != 6])
        dice = dice[:nr_not_six]
        nr_remaining.append(len(dice))
    return nr_remaining
