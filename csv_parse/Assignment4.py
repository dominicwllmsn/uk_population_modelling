# GBplaces_sorted
# Program which opens the GBplaces.csv file, ignores the headings row before 
# separating each column into their respective lists. It then sorts the 
# population list into ascending order (i.e. least populous place at the 
# top, most populous at the bottom), before creating a new .csv file and 
# writing the new data to it in the correct format.


# Open the GBplaces.csv file in read-only format.

placesFile = open('GBplaces.csv','r')
print('Opened file. The program is now reading in the data.')

# Create a list for each column of data
places,placeType,pop,lat,long = [],[],[],[],[]
i = 0  # Counter to assign the correct index to each tuple in the 'pop' list.

# Loop to go through each line, assign a variable firstLine to the heading
# row, then split each subsequent line into its columns and append each
# list with the correct data. Append the 'pop' list with tuples so that the 
# each population figure is still assigned to the correct index after ordering.
for line in placesFile:
    if line.startswith('%'):
        firstLine = line
        continue
    else:
        columns = line.split(',')
        places.append(columns[0])
        placeType.append(columns[1])
        pop.append((float(columns[2]),i))
        lat.append(columns[3])
        long.append(columns[4])
        i += 1

placesFile.close()

# Create new sorted population list. Sort according to the second element in 
# each tuple (i.e. the population data). 
pop_sorted = sorted(pop, reverse=False)

# Create a new file GBplaces_sorted.csv which is writable.
writeFile = open('GBplaces_sorted.csv','w')

# Write the heading row to the new file, before writing each row in population
# order.
writeFile.write(firstLine)
for popTuple in pop_sorted:
    popIndex = popTuple[1]
    writeFile.write('{0},{1},{2},{3},{4}'\
            .format(places[popIndex],placeType[popIndex],popTuple[0]\
                    ,lat[popIndex],long[popIndex]))
    
    
writeFile.close()

print('Done. A new file (GBplaces_sorted.csv) has been created which contains \
the data ordered according to increasing population size.')