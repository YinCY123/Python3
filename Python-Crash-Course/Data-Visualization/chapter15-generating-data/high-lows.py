import csv
from matplotlib import pyplot as plt
from datetime import datetime


# get dates and high temperatures from file.
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot data
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = "red", linewidth = 1)
plt.plot(dates, lows, c = "blue", linewidth = 1)
plt.fill_between(dates, lows, highs, facecolor = "blue", alpha = 0.1)

# format plot
plt.title(label = "Daily high and low temperatures - 2014", fontsize = 24)
plt.xlabel(xlabel = "", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel(ylabel = "Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = "major", labelsize = 10)

plt.show()