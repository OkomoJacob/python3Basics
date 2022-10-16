from random import randint


class Dice:
    def __init__(self):
        pass

    def roll(self):
        first = randint(1, 6)
        second = randint(1, 6)
        return (first, second)


# Create object named result
dice = Dice()
print(dice.roll())