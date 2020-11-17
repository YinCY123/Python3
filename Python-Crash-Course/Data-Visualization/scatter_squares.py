import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [a**2 for a in x_value]
plt.scatter(x_value, y_value, s = 10,
            edgecolors = "none",
            c = y_value,
            cmap = plt.cm.Blues)

# set chart title and label axes
plt.title(label = "Square Numbers", fontsize = 24)
plt.xlabel(xlabel="Value", fontsize = 14)
plt.ylabel(ylabel="Square of Value", fontsize = 14)

# set size of tick labels
plt.tick_params(axis = "both", which = "major", labelsize = 10)

plt.axis([0, 1100, 0, 1100000])
plt.savefig("squares_plot.pdf", bbox_inch = "tight")
