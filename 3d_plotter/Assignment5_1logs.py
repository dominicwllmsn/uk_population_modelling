# Assignment5.1 with log10
# Program which reads in and stores the population, latitude and longtude
# data from the 'GBplaces.csv' file before plotting the latitude of each entry
# against the corresponding longitude on the x- and y-axes of a 3D bar plot. 
# The height of each 3D bar  varies depending upon the population of the 
# town/city. The 3D bars are also coloured according to the value of the 
# base-10 log of their populations. The result is a map of the 100 most 
# populous locations on the British Isles
# Note to marker: The orientation of the plot was optimized on Campus PCs.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Open GBplaces.csv file and loop over each line in the file, appending the 
# population figures, latitude and longitude to the 'pop', 'lat' and 'long' 
# lists respectively.
placesFile = open('GBplaces.csv','r')
    
pop,lat,long = [],[],[]

for line in placesFile:
    if line.startswith('%'):
        continue
    else:
        splitLine = line.split(',')
        pop.append(int(splitLine[2]))
        lat.append(float(splitLine[3]))
        long.append(float(splitLine[4][:-1]))

placesFile.close()


# Construct both the 3D figure/environment as well as the x-,y- and z-axes.
fig = plt.figure()
axis = Axes3D(fig)

# Convert the pop, lat and long lists to numpy arrays. This is done to allow us
# to plot the values on the 3D graph as well as for easier arithmetic 
# manipulation. Assign Z to the base-10 log of the population array so that the
# large population range is fully represented on the plot.
X, Y, Z = np.array(long), np.array(lat), np.log10(np.array(pop))

# Create an array called 'colours'. Required to vary the colour of each 3D bar
# according to the population of the town/city. The colours array must be 
# normalized (i.e. have each element between 0 and 1) for it to properly 
# vary each town/cities colour according to the designated colormap (cmap).
# I chose the 'terrain' cmap as it spans a range of different colours, meaning
# that larger cities like London and Birmingham can be more easily recognised.
norm = plt.Normalize((Z).min(), (Z).max())
colours = plt.cm.terrain(norm(Z))


# Create the 3D bar plot with longitude on the x-axis, latitude on the y-axis
# and base-10 log of population on the z-axis. The dx,dy,dz arguments give
# the 'depth' or dimensions of the bar in each dimension. The color parameter
# takes the colours array as its argument, allowing the colour of the bars
# to vary with the colormap specified above.
plot1 = axis.bar3d(X,Y,Z,dx=0.3,dy=0.3,dz=Z/2.5,color=colours)

# Assign each axis the correct label.
axis.set_xlabel('\nLongitude (\u00B0)')
axis.set_ylabel('\nLatitude (\u00B0)')
axis.set_zlabel('\nlog10(Population)')
# Set the limits and 'ticks'/increments of the z-axis scale.
axis.set_zlim3d(4,7)
axis.set_zticks([4.5,5,5.5,6,6.5,7])
# Set the viewer's 'camera' orientation with different elevation and azimuthal 
# angle values (in degrees).
axis.view_init(elev=72,azim=-72)

# Create the colorbar for the plot by specifying the colormap (cmap) used 
# (terrain), before assigning the colorbar to the log-10 population array (Z) 
# and plotting it on the figure with the correct label.
colourMap = plt.cm.ScalarMappable(cmap=plt.cm.terrain)
colourMap.set_array(Z)
colBar = plt.colorbar(colourMap).set_label('log10(Population)')

plt.show()
