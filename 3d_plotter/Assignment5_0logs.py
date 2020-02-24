# Assignment5.0 with log10
# Program which reads in and stores the population, latitude and longtude data
# from the 'GBplaces.csv' file before plotting the longitude of each entry
# against the corresponding latitude on a scatter plot. The scatter plot points
# are coloured according to the base-10 log of their respective populations.
# The size of each scatter point also varies depending upon the population of
# the town/city. 

import matplotlib.pyplot as plt
from matplotlib import cm
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


# Create a numpy array of the pop list (for easier arithmetic manipulation) and 
# take the base-10 log of each of its elements
pop_log = np.log10(np.array(pop))

# Create a scatter plot of longitude on the x-axis and latitude on the y-axis.
# Vary the colour and size of the dots according to the corresponding
# population of the place. Colour each point using the chosen colormap (cmap).
# Include alpha argument to enhance the visual aspects of the plot.
plot1 = plt.scatter(long,lat,c=pop_log,s=np.array(pop)/25000,cmap=cm.winter_r,\
                    alpha=0.65)
# Create a colorbar for the plot so that the corresponding population figures
# can be found from a point's colour. Also assign labels to the x- and y-axis.
plt.colorbar(plot1).set_label('log\u2081\u2080(Population)')
plt.xlabel('Longitude (\u00B0)')
plt.ylabel('Latitude (\u00B0)')

plt.show()


    