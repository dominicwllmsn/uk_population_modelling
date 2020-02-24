# Assignment5.1

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


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


fig = plt.figure()
ax = Axes3D(fig)


x_array,y_array,z_array = np.array(long),np.array(lat),np.array(pop)
colours = plt.cm.terrain(z_array*2/(max(pop)))


plot1 = ax.bar3d(x_array,y_array,z_array,0.65,0.65,z_array*10,color=colours)
ax.set_xlabel('\nLongitude (\u00B0)')
ax.set_ylabel('\nLatitude (\u00B0)')
ax.set_zlabel('\n\nPopulation')
#ax.set_zticks([])
#ax.set_zlim3d(0,int(1e7))
ax.view_init(elev=65,azim=285)

m = plt.cm.ScalarMappable(cmap=plt.cm.terrain)
m.set_array(z_array)
cbar = plt.colorbar(m).set_label('\nPopulation')

plt.show()
