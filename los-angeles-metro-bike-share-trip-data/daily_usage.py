# Script for outputting daily usage accross days, seasons, weeks, etc.

import pandas as pd
import numpy as np
import geopy.distance
from statistics import mean
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv("metro-bike-share-trip-data.csv")
daily_usage = {}
sanitized_df = df.dropna(subset=["Passholder Type", 'Start Time'])

def increm_week(day):
    for day_k in daily_usage.keys():
        if abs((day - day_k).days) <= 3:
            daily_usage[day_k] += 1
            break
    else:
        daily_usage[day] = 1

def increm_day(day):
    if day in daily_usage:
        daily_usage[day] += 1
    else:
        daily_usage[day] = 1

def str_to_date(string):
    return datetime.strptime(string, "%Y-%m-%d")

for _, row in sanitized_df.iterrows():
    if row["Passholder Type"] in {"Monthly Pass", "Flex Pass", "Staff Annual", "Walk-up"}:
        day = str_to_date(row["Start Time"].split("T")[0]) # We only care about the day
        increm_day(day)

seasonal_usage = {"Spring":0, "Summer":0, "Fall":0, "Winter":0}
day_count = {"Spring":0, "Summer":0, "Fall":0, "Winter":0}
for k, v in daily_usage.items():
    to_place = k.timetuple().tm_yday
    if to_place in range(80, 172):
        seasonal_usage["Spring"] += v
        day_count["Spring"] += 1
    elif to_place in range(172, 264):
        seasonal_usage["Summer"] += v
        day_count["Summer"] += 1
    elif to_place in range(264, 355):
        seasonal_usage["Fall"] += v
        day_count["Fall"] += 1
    else:
        seasonal_usage["Winter"] += v
        day_count["Winter"] += 1

for k, v in seasonal_usage.items():
    seasonal_usage[k] = seasonal_usage[k] / day_count[k]

plt.scatter(seasonal_usage.keys(), seasonal_usage.values())
plt.xlabel("Season")
plt.ylabel("Regular-Membership Usage")
plt.title("Seasonal Usage")
fig = plt.gcf()
fig.savefig("bike_usage_seasonally.png")