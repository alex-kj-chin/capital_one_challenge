# A Note About Developmental Code

The code in this repository is very exploratory/developmental. It is in no way production ready. As the objective in this assignment was to generate effective visualizations and understand the data, I thought this would be the best way to achieve that goal. I have attempted to place comments throughout to annotate my work, but I would advise consulting the [web report](https://alex-kj-chin.github.io/cayman/) for methodology.

# Structure

The entirety of the code is in the `los-angeles-metro-bike-share-trip-data` folder. I describe each of the scripts briefly

 - `daily_usage.py`: This gives the number of rides and can be configured to calculate these statistics over various timeframes.
 - `Bonus 1.ipynb`, `Bonus 2.ipynb`, `Bonus 3.ipynb`: Exploration for each of the bonus problems is in its own jupyter notebook, labeled appropriately.
 - `general_calculations.ipynb`: This file contains my preliminary data exploration and some work on arrival/departure counts and travel times
 - `general_stats.py`: This script calculates arrivals and departures accounting for round trips and other various factors
 - `graph_bikes.py`: This script graphs the bike mileage
 - `make_weekday_breakdown.py`: This script graphs the ridership (absolute number and duration) by day of the week
 - `Required Questions.ipynb`: This jupyter notebook contains a lot of preliminary data work that I later visualized with more formal scripts.
 - `revenue_pie.py`: This script graphed the pie chart for revenue breakdown
 - `seasonal_grapher.py`: This script made the stacked bar graph for seasonal ridership