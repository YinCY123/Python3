from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        self.direction = choice([-1, 1])
        self.distance = choice(list(range(10)))
        self.step = self.direction * self.distance
        return self.step

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)