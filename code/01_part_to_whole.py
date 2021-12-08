import matplotlib.pyplot as plt

# create data
names = ['Tetris', 'Poker', 'Squash', 'Chess Bot', 'Homework']
size = [15,10,10,10,5]
 
# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='white')

# Custom wedges
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title('How I Spend My Free Time')
plt.savefig('../creations/01_part_to_whole.png')