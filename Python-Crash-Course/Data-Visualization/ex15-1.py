import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [a**3 for a in x_value]
plt.scatter(x_value, y_value, s = 20, c = y_value, cmap = plt.cm.jet)
plt.show()