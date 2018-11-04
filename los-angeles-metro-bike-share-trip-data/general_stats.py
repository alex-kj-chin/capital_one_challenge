import pandas as pd
import numpy as np
df = pd.read_csv("metro-bike-share-trip-data.csv", low_memory=False)
print("Mean: ", df["Duration"].mean())

station_start = {}
station_end = {}

def increm_dict(dictionary, key):
	if key != np.nan:
		if key in dictionary:
			dictionary[key] += 1
		else:
			dictionary[key] = 0

df["Starting Station ID"].map(lambda x: increm_dict(station_start, x))
df["Ending Station ID"].map(lambda x: increm_dict(station_end, x))
np.save("test.npy", station_start)