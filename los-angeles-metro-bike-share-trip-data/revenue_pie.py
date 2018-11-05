import math
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metro-bike-share-trip-data.csv")
revenue = {'Monthly Pass': 0, 'Flex Pass':0, 'Walk-up': 0 , 'Staff Annual':0}

sanitized_df = df.dropna(subset=['Passholder Type', 'Duration'])
for _, row in sanitized_df.iterrows():
    if row['Duration'] > 1800:
        revenue[row["Passholder Type"]] += 1
        # revenue[row["Passholder Type"]] += math.ceil((row['Duration'] - 1800) / 1800)

plt.pie(revenue.values(), labels=revenue.keys())
fig = plt.gcf()
fig.savefig("overtime_pie.png")