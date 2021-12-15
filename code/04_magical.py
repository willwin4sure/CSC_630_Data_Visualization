import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (15,3)


years = np.array([2000+i for i in range(21)])

# data from https://www.landofbasketball.com/teams/records_miami_heat.htm
orlando_magic_win_percentages = [.524,.537,.512,.256,.439,.439,.488,.634,.720,.720,.634,.561,.244,.280,.305,.427,.354,.305,.512,.452,.292]
miami_heat_win_percentages = [.610,.436,.305,.512,.720,.634,.537,.183,.524,.573,.707,.697,.805,.659,.451,.585,.500,.537,.476,.603,.556]

# make a matplotlib bar graph between these two values with years as x axis
width = 0.3
plt.bar(years-0.15, orlando_magic_win_percentages, width, color='blue', label='Orlando Magic')
plt.bar(years+0.15, miami_heat_win_percentages, width, color='red', label='Miami Heat')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Win Percentage')
plt.savefig('04_magical.png')
