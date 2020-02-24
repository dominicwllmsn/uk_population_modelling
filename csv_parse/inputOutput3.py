# inputOutput3

placesFile = open('GBplaces.csv','r')

places,placeType,pop,lat,long = [],[],[],[],[]

for line in placesFile:
    if line.startswith('%'):
        firstLine = line
        continue
    else:
        splitLine = line.split(',')
        places.append(splitLine[0])
        placeType.append(splitLine[1])
        pop.append(splitLine[2])
        lat.append(splitLine[3])
        long.append(splitLine[4])

placesFile.close()


writeFile = open('GBtowns.csv','w')

writeFile.write(firstLine)
for i in range(len(placeType)):
    if placeType[i] == 'Town':
        writeFile.write('{0},{1},{2},{3},{4}\n'\
                        .format(places[i],'Town',pop[i],lat[i],long[i]))
    else:
        continue
    
writeFile.close()