# Assignment5.0

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


placesFile = open('GBplaces.csv','r')

places,placeType,pop,lat,long = [],[],[],[],[]


for line in placesFile:
    if line.startswith('%'):
        continue
    elif line.startswith('London'):
        splitLine = line.split(',')
        pop_Lon = int(splitLine[2])
        lat_Lon = float(splitLine[3])
        long_Lon = float(splitLine[4][:-1])
    else:
        splitLine = line.split(',')
        places.append(splitLine[0])
        pop.append(int(splitLine[2]))
        lat.append(float(splitLine[3]))
        long.append(float(splitLine[4][:-1]))

placesFile.close()


pop_log = np.log10(np.array(pop))
###
Z = [[0,0],[0,0]]
levels = range(0,int(1.2e6),int(1e5))
CS3 = plt.contourf(Z, levels, cmap='winter')
plt.clf()
###
plot1 = plt.scatter(long,lat,c=pop,s=np.array(pop)/5000,cmap=cm.winter,\
                    vmin=0,vmax=int(1e6),alpha=0.6)
plot2 = plt.scatter(long_Lon,lat_Lon,c='#FDFF7A',s=pop_Lon*0.00016,alpha=0.7)
plt.colorbar(CS3).set_label('Population')
plt.xlabel('Longitude (\u00B0)')
plt.ylabel('Latitude (\u00B0)')

plt.show()


    