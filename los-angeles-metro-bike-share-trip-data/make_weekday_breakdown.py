import matplotlib.pyplot as plt

weekday_usage = [17251, 19136, 19819, 20345, 20043, 18530, 17303]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.bar(range(7), weekday_usage, tick_label=days)
plt.title("Usage by Weekday")
plt.ylabel("Total Usage (over full timeframe)")
plt.xlabel("Day")
fig = plt.gcf()
fig.savefig("weekday_usage.png")

walk_usage = [4386, 4032, 4288, 4804, 5815, 9054, 8845]

plt.bar(range(7), walk_usage, tick_label=days)
plt.title("Usage by Weekday")
plt.ylabel("Total Usage (over full timeframe)")
plt.xlabel("Day")
fig = plt.gcf()
fig.savefig("walk_usage.png")

duration_usage = [23855220, 22483440, 25165080, 25460280, 30741120, 37264800, 40993980]

plt.close()
plt.bar(range(7), walk_usage, tick_label=days)
plt.title("Usage by Weekday")
plt.ylabel("Total Duration of Usage (over full timeframe)")
plt.xlabel("Day")
fig = plt.gcf()
fig.savefig("duration_usage.png")