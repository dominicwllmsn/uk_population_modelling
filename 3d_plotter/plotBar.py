# plotBar.py
# program to read some data and plot a bar graph

# import the module
import matplotlib.pyplot as plt;

# open the file
readFile = open('namesAges.csv','r');

# create empty arrays
names = [];
ages = [];

# read in the file line by line
for line in readFile:
    # split the input line based on a comma
    splitUp = line.split(',');

    # store the values in the arrays
    names.append(splitUp[0]);
    ages.append(int(splitUp[1].strip()));

# close the file
readFile.close();

# create an array of numbers from 0 to length(names)
bars = range(0,len(names));

# plot a horizontal bar graph of people and their ages
plt.barh(bars,ages);

# add a title
plt.title('People and Their Ages');

# label the axes
plt.xlabel('Ages');
plt.ylabel('Person');

# control the tick labels
plt.yticks(bars,names);

# show the graph
plt.show();

