import matplotlib.pyplot as plt

data = [['China', 1400, 732], ['India', 1380, 1090], ['U.S.', 325, 336], ['Indonesia',258,229], ['Pakistan',214,248],['Brazil',212,165], ['Nigeria',206,791],['Bangladesh',157,81],['Russia',146,106],['Japan',128,60]]

for data_point in data:
    plt.plot([2017,2020],[data_point[1],data_point[2]], marker='o', label=data_point[0])

plt.legend(loc = 'upper right')
plt.ylabel("Population in Millions of People")

plt.savefig('05_slope.png')