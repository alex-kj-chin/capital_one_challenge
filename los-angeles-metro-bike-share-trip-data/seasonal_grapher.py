import matplotlib.pyplot as plt

monthly = [317.84615384615387, 274.1818181818182, 391.5733333333333, 219.73626373626374]
walk = [158.28571428571428, 149, 203.8, 108.74725274725274]
flex = [33.2967032967033, 37.09090909090909, 53.64, 22.593406593406595]

for x in range(4):
	walk[x] += flex[x]
	monthly[x] += walk[x]

width = 0.35

ind = range(4)

p1 = plt.bar(ind, monthly, width)
p3 = plt.bar(ind, walk, width)
p2 = plt.bar(ind, flex, width)

plt.title("Seasonal Segmentation")
plt.xlabel("Season")
plt.ylabel("Bike Rides")
plt.xticks(range(4),["Fall", "Spring", "Summer", "Winter"])
plt.legend([p1, p3, p2], ['Monthly', 'Walk-Up', "Flex"])
fig = plt.gcf()
fig.savefig("seasonal_stacked.png")