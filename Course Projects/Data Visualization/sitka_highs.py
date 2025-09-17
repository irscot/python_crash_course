import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    print(highs)

# Plot high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Tempearature (F)', fontsize=16)

# Displays dates diagonally.
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
