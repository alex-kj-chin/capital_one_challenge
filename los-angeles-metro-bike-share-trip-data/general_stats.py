# Jupyter was having some issues generating graph labels, so I generated the graphs in a script

import pandas as pd
import numpy as np
import geopy.distance
from statistics import mean
import matplotlib.pyplot as plt
from datetime import datetime

def str_to_date(string):
    return datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")

df = pd.read_csv("metro-bike-share-trip-data.csv")

station_start = {}
station_end = {}

def increm_dict(dictionary, key):
    if key != np.nan:
        if key in dictionary:
            dictionary[key][0] += 1
        else:
            dictionary[key] = [1, "2022-07-07T04:17:00", "2011-07-07T04:17:00"] # Arbitrary ISO later/earlier than all dates in data set

# Check dates for normalization
sanitized_df = df.dropna(subset=["Starting Station ID", "Ending Station ID", 'Start Time', 'End Time'])
for _, row in sanitized_df.iterrows():
    increm_dict(station_start, row["Starting Station ID"])
    increm_dict(station_end, row["Ending Station ID"])
    if row["Start Time"] < station_start[row["Starting Station ID"]][1]:
        station_start[row["Starting Station ID"]][1] =  row["Start Time"]
    if row["Start Time"] < station_end[row["Ending Station ID"]][1]:
        station_end[row["Ending Station ID"]][1] =  row["Start Time"]
    if row["End Time"] > station_start[row["Starting Station ID"]][2]:
        station_start[row["Starting Station ID"]][2] = row["End Time"]
    if row["End Time"] > station_end[row["Ending Station ID"]][2]:
        station_end[row["Ending Station ID"]][2] = row["End Time"]

station_start = {k: v[0] / ((str_to_date(v[2]) - str_to_date(v[1])).days) for k, v in station_start.items()} # Normalize over number of days
station_end = {k: v[0] / ((str_to_date(v[2]) - str_to_date(v[1])).days) for k, v in station_end.items()}

# Normalize and data wrangling
end_pairs = list(station_end.items())
end_pairs.sort(key=lambda x: x[1], reverse=True)
total_ends = 0
for pair in end_pairs:
    total_ends += pair[1]
end_pairs = list(map(lambda x: (x[0], x[1], x[1] / total_ends), end_pairs))
endings = set(map(lambda x: x[0], end_pairs[:10]))
hist_end = list(map(lambda x: x[1], end_pairs))
start_pairs = list(station_start.items())
start_pairs.sort(key=lambda x: x[1], reverse=True)
total_starts = 0
for pair in end_pairs:
    total_starts += pair[1]
start_pairs = list(map(lambda x: (x[0], x[1], x[1] / total_starts), start_pairs))
starts = set(map(lambda x: x[0], start_pairs[:10]))
hist_start = list(map(lambda x: x[1], start_pairs))

# Print top 5
print(start_pairs[:5])
print(end_pairs[:5])

# Calculate overlap of top 10
print(starts.intersection(ends))

# Graphing
plt.hist(hist_start, facecolor='orange', bins=50)
plt.title("Histogram of Departure Counts in Stations")
plt.ylabel("Number of Stations")
plt.xlabel("Number of Departures")
fig = plt.gcf()
fig.savefig("departure_hist.png")

plt.close()
plt.hist(hist_end, facecolor='purple', bins=50)
plt.title("Histogram of Arrival Counts in Stations")
plt.ylabel("Number of Stations")
plt.xlabel("Number of Arrivals")

fig = plt.gcf()
fig.savefig("arrivals_hist.png")