import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk, and plot the points
# keep making new walks, as long as the program is active.

while True:
    # make a random walk, and plot the points.
    rw = RandomWalk(num_points = 5000)
    rw.fill_walk()

    # set the size of the plotting window.
    # figure size in inches
    plt.figure(figsize = (10, 6), dpi = (100))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_value,
                rw.y_value,
                linewidth = 1)

    # emphasize the first and last points
    plt.scatter(0, 0,
                c = "green",
                edgecolors="none",
                s = 50)

    plt.scatter(rw.x_value[-1],
                rw.y_value[-1],
                c = "red",
                edgecolors="none",
                s = 50)

    # remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("make another walk? (y/n):")
    if keep_running == "n":
        break