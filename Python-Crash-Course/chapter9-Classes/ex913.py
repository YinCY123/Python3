from random import randint
class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self, sides, times):
        res = []
        for i in range(1, times + 1):
            s = randint(1, sides)
            res.append(s)
        print(res)


d = Die()
d.roll_die(sides=10, times=10)
d.roll_die(sides=20, times=10)